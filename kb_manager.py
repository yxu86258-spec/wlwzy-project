#!/usr/bin/env python
"""
Karpathy风格知识库管理工具
"""

import os
import sys
import argparse

def run_command(script_name, args=None):
    """运行脚本"""
    script_path = os.path.join('scripts', f'{script_name}.py')
    if not os.path.exists(script_path):
        print(f"❌ 脚本未找到: {script_path}")
        return False
    
    cmd = f'python {script_path}'
    if args:
        cmd += f' {args}'
    
    print(f"执行: {cmd}\n")
    result = os.system(cmd)
    return result == 0

def main():
    parser = argparse.ArgumentParser(description='Karpathy风格知识库管理工具')
    subparsers = parser.add_subparsers(dest='command', help='命令')
    
    # 导入命令
    subparsers.add_parser('ingest', help='导入原始资料 (PDF/网页/图片)')
    
    # 编译命令
    compile_parser = subparsers.add_parser('compile', help='编译知识库')
    compile_parser.add_argument('-i', '--incremental', action='store_true', 
                               help='使用增量编译')
    
    # 检查命令
    subparsers.add_parser('check', help='检查编译策略')
    subparsers.add_parser('lint', help='健康检查')
    
    # 问答命令
    subparsers.add_parser('query', help='启动问答系统')
    subparsers.add_parser('chat', help='启动多轮对话')
    
    # 可视化命令
    subparsers.add_parser('visualize', help='生成知识图谱')
    
    # 导出命令
    export_parser = subparsers.add_parser('export', help='导出知识库')
    export_parser.add_argument('-f', '--format', choices=['html', 'markdown', 'pdf'],
                              default='html', help='导出格式')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # 执行命令
    if args.command == 'ingest':
        run_command('ingest')
    
    elif args.command == 'compile':
        if args.incremental:
            print("⚡ 执行增量编译检查...")
            run_command('incremental_check')
        run_command('compile')
    
    elif args.command == 'check':
        run_command('incremental_check')
    
    elif args.command == 'lint':
        run_command('lint')
    
    elif args.command == 'query':
        run_command('query')
    
    elif args.command == 'chat':
        run_command('query')  # chat 就是 query
    
    elif args.command == 'visualize':
        run_command('visualize')
    
    elif args.command == 'export':
        run_command('export', f'--format {args.format}')

if __name__ == '__main__':
    main()