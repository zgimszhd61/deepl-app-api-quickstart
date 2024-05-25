# 使用LibreOffice将DOCX内容转化为PDF格式.

import subprocess

def convert_docx_to_pdf(docx_path, pdf_path):
    """
    使用LibreOffice将DOCX文件转换为PDF文件。
    
    参数:
    - docx_path: DOCX文件的路径。
    - pdf_path: 生成的PDF文件的存储路径。
    """
    try:
        # 构建LibreOffice的命令行命令
        cmd = [
            '/Applications/LibreOffice.app/Contents/MacOS/soffice',
            '--headless',
            '--convert-to',
            'pdf',
            '--outdir',
            pdf_path,
            docx_path
        ]
        
        # 执行命令
        subprocess.run(cmd, check=True)
        print("转换成功！")
    except subprocess.CalledProcessError as e:
        print("转换失败：", e)

# 示例：将当前目录下的example.docx转换为PDF，并保存在同一目录下
convert_docx_to_pdf('2405.14838v1.docx', '.')