# 将内容翻译成PDF格式转翻译成中文PDF.

import deepl
from dotenv import load_dotenv
import os
load_dotenv()
secret_key = os.getenv('APIKEY')


# 替换为你的DeepL API密钥
auth_key = secret_key

# 创建一个Translator实例
translator = deepl.Translator(auth_key)

# 指定要翻译的PDF文档的路径和翻译后文档的保存路径
input_path = "2405.12862v1.pdf"
output_path = "2405.12862v1.docx"  # 注意：翻译后的文档将是.docx格式

try:
    # 使用translate_document_from_filepath()函数上传和翻译文档
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="ZH",  # 目标语言代码，这里改为简体中文
    )
except deepl.DocumentTranslationException as error:
    # 如果在文档已上传后翻译过程中发生错误
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading {error}, id: {doc_id} key: {doc_key}")
except deepl.DeepLException as error:
    # 如果在上传过程中发生错误
    print(error)