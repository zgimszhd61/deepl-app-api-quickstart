# deepl-app-api-quickstart

要使用DeepL的API翻译PDF文档，你需要遵循几个步骤来实现这个过程。以下是一个基于DeepL API文档和官方Python库的示例，展示如何上传PDF文档进行翻译，并下载翻译后的文档。

首先，确保你已经注册了DeepL API，并获取了API密钥。接下来，你可以使用DeepL的官方Python库来简化API调用的过程。

```python
import deepl

# 替换为你的DeepL API密钥
auth_key = "your_auth_key_here"

# 创建一个Translator实例
translator = deepl.Translator(auth_key)

# 指定要翻译的PDF文档的路径和翻译后文档的保存路径
input_path = "/path/to/your/document.pdf"
output_path = "/path/to/translated_document.docx"  # 注意：翻译后的文档将是.docx格式

try:
    # 使用translate_document_from_filepath()函数上传和翻译文档
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="DE",  # 目标语言代码，这里以德语为例
    )
except deepl.DocumentTranslationException as error:
    # 如果在文档已上传后翻译过程中发生错误
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading {error}, id: {doc_id} key: {doc_key}")
except deepl.DeepLException as error:
    # 如果在上传过程中发生错误
    print(error)
```

这个示例首先导入`deepl`模块，并使用你的DeepL API密钥创建一个`Translator`实例。然后，它指定了要翻译的PDF文档的路径和翻译后文档的保存路径。`translate_document_from_filepath()`函数用于上传PDF文档并请求翻译，目标语言通过`target_lang`参数指定。如果在翻译过程中发生任何错误，异常处理部分将捕获这些错误并打印相关信息。

请注意，这个示例假设你已经安装了DeepL的官方Python库。如果还没有安装，你可以通过运行`pip install deepl`来安装它[10]。

此外，DeepL API允许你在上传文档时选择不同的输出格式。默认情况下，翻译后的文档将以与输入文档相同的格式返回。但是，你可以使用`output_format`参数在上传文档时选择不同的输出格式，例如，将PDF文件翻译为可编辑的Microsoft Word文档（DOCX），以便根据需要进行进一步的更改[6]。

Citations:
[1] https://www.deepl.com/zh/blog/deepl-launches-in-house-pdf-translation-for-improved-security-and-efficiency
[2] https://www.deepl.com/zh/blog/deepl-pdf-files-translation
[3] https://www.deepl.com/en/features/document-translation/pdf
[4] https://www.deepl.com/en/blog/deepl-pdf-files-translation
[5] https://www.deepl.com/zh/features/document-translation/pdf
[6] https://developers.deepl.com/docs/api-reference/document
[7] https://developers.deepl.com/docs
[8] https://www.deepl.com/zh/features/document-translation
[9] https://www.deepl.com/pro-api
[10] https://github.com/DeepLcom/deepl-python
[11] https://developers.deepl.com/docs/api-reference/document/openapi-spec-for-document-translation
[12] http://transtech.lingosail.com/news/detail/189425/cn
[13] https://support.deepl.com/hc/zh-cn/articles/4408150502802-%E7%BF%BB%E8%AF%91-PDF-%E6%96%87%E4%BB%B6
[14] https://blog.csdn.net/zt5169/article/details/138462442
[15] https://support.deepl.com/hc/zh-cn/articles/4411308018450-PDF-%E6%96%87%E4%BB%B6%E7%BF%BB%E8%AF%91
[16] https://support.deepl.com/hc/en-us/articles/360020582359-Document-formats
