# 如何对大模型进行知识库外挂

*   日期 2024.5.6
*   作者 蔡俊志

## 理论部分

外挂知识库指的是在不改变模型结构（权重）的情况下，使得模型能够引用一些用户提供的新知识（比如一份文档）来参与其回答的生成的技术。

下面是一些例子：

*   给模型外挂十份简历文件，让模型找出其中有Python编程经验的候选人
*   给模型外挂一份说明书，询问模型某一具体步骤的细节
*   给模型外挂一大堆某个领域的论文，让模型总结一下使用的方法

下面这张图展示了知识库外挂的具体实现细节。

![](data:image/webp;base64,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)


我们可以把整个过程抽象为下面的这些步骤。

Step1：将新知识数据生成一个向量数据库：

*   Step1.1：将需要挂载的文档（可以是pdf、txt、甚至是ppt文件）用文本切割器进行切割，按段落或者是句子切割成一块一块的。
*   Step1.2：将这些一块一块的切割出来的文字用Embedding模型（比如BERT、M3E等）编码成一定长度的向量，然后存入向量数据库。

Step2：根据用户的问题，从向量数据库中找出相关的文字片段，并将这些“参考文本"和用户的问题结合起来送入模型。

*   Step2.1: 将用户的问题用上面相同的Embedding模型编码为向量，再从向量中找出 $k$ 个相似向量的对应知识库文本片段，这个相似度的衡量方式可以是cosine相似度等。
*   Step2.2：将上一步得到的 $k$ 个知识库文本片段和用户的问题利用一个固定的Prompt模板结合，然后输入模型进行预测。


下面这个解释十分的形象易懂，引用自[链接](https://blog.csdn.net/lgnlgn/article/details/131989563)

>简单的说就是根据用户问题，从知识库获取与 __问题__ 相关的 __文档片段__，把这些 __文档片段__ 和 __问题__ 本身结合起来一起喂给大模型，然后让大模型根据 __文档片段__ 来回答 __问题__。这里就涉及到一个如何获取 __问题__ 相关的 __文档片段__ 的过程了，其实可以直接用文本检索方式，但传统的全文检索由于是词的匹配，因此对纯粹的问句效果可能不好。因此现在主流的方式是用向量匹配，就是把 __问题__ 和知识库的文本都转成向量，再用向量的近似搜索获取更为相关的结果。



## 实验

*   实验环境

*   运行资源
内存： 32GB
GPU： RTX 4090 24GB




在下面的部分，首先我会介绍一下基础的聊天代码。然后，我将会展示两种外挂知识库的实现代码（如下所示）

*   实现代码1：比较好理解，比较简单直白的实现代码 （chromadb）
*   实现代码2：更贴近实际应用场景的实现代码 （langchain + chromadb）

它们使用的Embedding预训练模型均为 m3e-large，使用的chat模型均为ChatGLM3-6B。

### 基础聊天代码

首先导入需要的库以及聊天模型（也就是ChatGLM3-6B）

```python
import os
import platform
from transformers import AutoTokenizer, AutoModel
import hashlib

MODEL_PATH = os.environ.get('MODEL_PATH', "/home/cjz/llms/THUDM/chatglm3-6b")
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()
```

下面的这部分使用了model的stream_chat API，其返回的是一个异步的generator，每次大模型吐出新的token的时候，就会进入新一轮的for循环，然后得到一个新的response。此时，` response[current_length:] ` 即为本轮产生大模型吐出的新的token，我们需要在每轮训话都打印这个新产生的token，这样就实现了一个一个吐字的效果。


```python
def main():
    past_key_values, history = None, []
    while True:
        query = input("\nEnter：")
        print("\nAnswer：", end="")
        current_length = 0
        for response, history, past_key_values in model.stream_chat(tokenizer, query, history=history, top_p=1,
                                                                    temperature=0.01,
                                                                    past_key_values=past_key_values,
                                                                    return_past_key_values=True):
            print(response[current_length:], end="", flush=True)
            current_length = len(response)
        print("")

if __name__ == "__main__":
    main()
```

接下来我们将在这个代码的基础上来进行知识库挂载的操作

他们都由以下部分组成

*   处理用户提供的知识库
*   创建向量数据库
*   查询数据库、使用Prompt模板

### 外挂知识库实现代码1

实现代码1只是为了更快的理解，因此这个实现精简了很多功能，且只有一个代码脚本，为了讲解清晰，代码段的代码顺序可能不是最终顺序，以文章末尾给出的完整代码为准。

#### 处理用户提供的知识库

这段代码获取用户的知识库（假设知识库储存的形式均为txt）

```python
texts = []
for filename in glob.glob("../knowledge_docs/*.txt"):
    with open(filename, encoding='utf-8') as f:
        texts.append(f.read())
```

#### 创建向量数据库


将上一步得到的texts代码用存放于 `'/home/cjz/models/m3e-large'` 的模型来进行编码，得到其嵌入向量，然后存放至 chromadb数据库备用，如果你不了解chromedb的话，可移步至[chromedb](https://docs.trychroma.com/)

```python
model = SentenceTransformer('/home/cjz/models/m3e-large')
embeddings = model.encode(texts).tolist()
collection = client.get_or_create_collection("test_collection")
ids = [f'id{x + 1}' for x in range(len(texts))]
collection.add(ids=ids, embeddings=embeddings, documents=texts)
```

可以看到这份代码简单起见未对原文本进行切割，毕竟只是为了理解。

#### 查询向量数据库、使用Prompt模板

有了向量数据库，当用户发出一个问题时，我们就需要在数据库中查找和这个问题有关的文字片段，下面的代码即为此功能。首先还是用m3e（注意这里必须和建立数据库时使用的嵌入模型一致）来将用户的问题编码为向量，然后用它在数据库中查找与其相似的向量，并取回相似向量对应的文本，这里我们设置 `n_results=1` 代表找到top1最相似的向量。

```python
def query_related(text: str, model: SentenceTransformer, coll):
    embedding = model.encode(text).tolist()
    result = coll.query(query_embeddings=embedding, n_results=1)['documents']
    return result[0][0]
```

注意，这里的 `n_results` 参数指的是要从数据库中查找的相似文本向量的数量，也可以理解为对知识库的 “引用量”。

好了，现在可以进入下一步了。在基础聊天代码中，我们将通过 `query = input("\nEnter：")` 得到的问题直接喂给了模型。至于现在，我们则需要在中间增加两行代码：

```python
query = input("\nEnter：")
related_text = query_related(query, embeddings_encoder, embeddings_db)
knowledge_embedded_query = f"'''\n{related_text}\n''' \n请上文提取信息并且结合你自己的判断和推理回答下面这个问题：“{query}”，如果这个问题和给你的上下文完全无关的话，就忘记这些上下文信息，然后正常的回答问题"

for response, history, past_key_values in model.stream_chat(tokenizer, knowledge_embedded_query, history=history, top_p=1,
                                                                    temperature=0.01,
                                                                    past_key_values=past_key_values,
                                                                    return_past_key_values=True):
    ...
```

下面这便是是我们的prompt模板。
>f"'''\n{related_text}\n''' \n请上文提取信息并且结合你自己的判断和推理回答下面这个问题：“{query}”，如果这个问题和给你的上下文完全无关的话，就忘记这些上下文信息，然后正常的回答问题"


### 外挂知识库实现代码2

#### 第一步：处理用户提供的知识库

我们可以使用langchain的各种库来适配用户可能会上传的多种格式的文件，首先我们载入这些库函数


```python
from langchain.document_loaders import (
    CSVLoader,EverNoteLoader,
    PDFMinerLoader,TextLoader,
    UnstructuredEmailLoader,UnstructuredEPubLoader,
    UnstructuredHTMLLoader,UnstructuredMarkdownLoader,
    UnstructuredODTLoader,UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader, UnstructuredExcelLoader,
)
```

然后创建拓展名和这些载入函数的映射关系，制作为 `LOADER_MAPPIG`

```python
LOADER_MAPPING = {
    ".csv": (CSVLoader, {}),".doc": (UnstructuredWordDocumentLoader, {}),".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),".eml": (MyElmLoader, {}),".epub": (UnstructuredEPubLoader, {}),".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),".odt": (UnstructuredODTLoader, {}),".pdf": (PDFMinerLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),".pptx": (UnstructuredPowerPointLoader, {}),".txt": (TextLoader, {"encoding": "utf8"}),
    ".xls": (UnstructuredExcelLoader, {}),".xlsx": (UnstructuredExcelLoader, {}),
}
```

有了这样一个 `LOADER_MAPPING` 之后，我们可以写一个函数用于加载单个文件

```python
def load_single_document(file_path: str) -> List[Document]:
    ext = "." + file_path.rsplit(".", 1)[-1]
    if ext in LOADER_MAPPING:
        loader_class, loader_args = LOADER_MAPPING[ext]
        loader = loader_class(file_path, **loader_args)
        return loader.load()

    raise ValueError(f"Unsupported file extension '{ext}'")
```

有了加载单个文件的函数，我们可以在这个基础上写出加载某个目录下全部文件的函数

```python
def load_documents(source_dir: str, ignored_files: None) -> List[Document]:
    """
    Loads all documents from the source documents directory, ignoring specified files
    """
    ignored_files = [] if ignored_files is None else ignored_files
    all_files = []
    for ext in LOADER_MAPPING:
        all_files.extend(
            glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
        )
    filtered_files = [file_path for file_path in all_files if file_path not in ignored_files]

    with Pool(processes=os.cpu_count()) as pool:
        results = []
        with tqdm(total=len(filtered_files), desc='Loading new documents', ncols=80) as pbar:
            for i, docs in enumerate(pool.imap_unordered(load_single_document, filtered_files)):
                results.extend(docs)
                pbar.update()

    return results
```

直接从文档中获取的文字往往很大，我们需要像前文提到的那样把这样一大块文字按照某种规则切成一小块一小块的，这样方便存储，也方便查询，同时也能更灵活的嵌入用户的问题。为了做到这一点，我们需要langchain提供的 `RecursiveCharacterTextSplitter` 这是一个非常棒的用于 _智能_ 切割文字的函数，其切割规则和使用方法可以在 [这里](https://zhuanlan.zhihu.com/p/650876562) 找到。

利用  `RecursiveCharacterTextSplitter`  ，我们可以像这样写一个函数用于切割上面得到的文字

```python
def process_documents(ignored_files: List[str] = None) -> List[Document]:
    """
    Load documents and split in chunks
    """
    ignored_files = [] if ignored_files is None else ignored_files
    print(f"Loading documents from {source_directory}")
    documents = load_documents(source_directory, ignored_files)

    if not documents:
        print("No new documents to load")
        exit(0)
    print(f"Loaded {len(documents)} new documents from {source_directory}")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
    return texts
```

#### 第二步：创建词向量数据库

经过上面的流程，我们应该已经得到了一个装满 _"切片文字"_ 的list了，现在我们需要把这些 _"切片文字"_ 用 m3e 进行编码得到它们的嵌入向量，然后把嵌入向量存入 chromadb。存入chromadb的过程非常简单，以至于我们不需要额外包装成一个函数，只需像下面这样写就可以了。

```python
def main():
    print("Creating new vectorstore")
    texts = process_documents()
    print(f"Creating embeddings. May take some minutes...")
    embedding_function = SentenceTransformerEmbeddings(model_name=embeddings_model_name)
    db = Chroma.from_documents(texts, embedding_function, persist_directory=output_dir)
    db.persist()
    print("Done")
```

可以看到这个数据库和上面的那个 _实现代码1_ 的数据库的最大区别在于，这里我们对数据库进行了持久化操作（也就是保存到硬盘里），保存位置为 `output_dir` 。当我们运行完这个main函数之后，我们就能得到一个随时取用的，位于 `output_dir` 知识数据库了


#### 第三步：查询数据库、使用Prompt模板

由于这里我们对数据库进行了持久化，因此对数据库的查找和读取方面的代码有一些不一样，其他基本一致，__这里只会介绍相比实现代码1里有变动的部分。__

首先是，我们可以通过下面的语句，然后传入一个数据库路径来读取上一步持久化后的数据库，注意，这里还传入了embedding_function，在这里也就是m3e。

```python
db = Chroma(persist_directory=output_dir, embedding_function=embedding_function)
```

当用户输入问题之后，我们可以简单的通过这个方式来直接找出和用户提问有关的知识库文本片段，由于在初始化db实例的时候已经传入了embedding_function，我们在这里就不用显式的手动对问题文本进行编码，similarity_search函数会帮我们完成这一步骤，直接传入字符串即可。

```python
response = db.similarity_search(query, k=3)
```

类似的，这里的k指的是要从数据库中查找的相似文本向量的数量，可以理解为对知识库的 “引用量”。

接下来，把这些获得的文本片段和用户的Query用模版结合起来就可以像之前的例子一样传给模型了。

```python
relevant_information = ''.join(str([document.page_content for document in response]))
        knowledge_embedded_query = f"'''\n{relevant_information}\n''' \n请上文提取信息并且结合你自己的判断和推理回答下面这个问题：“{query}”，如果这个问题和给你的上下文并没有明显的关系，就忘记这些上下文信息，然后正常的回答问题"
```

### 实验


#### 效果

下面开始实验，我将来自苹果的这份53页的 [iOS安全保护白皮书](https://www.apple.com.cn/iphone/business/docs/iOS_Security_Guide.pdf) 用上面的代码生成了一个向量数据库，设置的参数为：最大chuck=2000个token，嵌入模型：m3e-large，最大引用量（k）：3，使用的语言模型为 ChatGLM-6B-Chat（无量化）

*   问题一：我想了解iOS访问 Safari 已存储的密码方面的安全技术规格等内容
    *   __外挂知识库前的回答:__ 
    根据我所了解的信息，在 iOS 中，Safari 存储的密码是使用加密技术进行保护的。这些密码是以加密形式存储在设备上的，并且在使用时会进行解密。
    具体来说，Safari 使用的密码是使用 AES-256 加密算法进行加密的。
    ...
    总的来说，iOS 中 Safari 存储的密码是使用加密技术进行保护的，并且在使用时会进行解密。这样可以确保密码的安全性。
    *   __外挂知识库后的回答:__ 
    首先，iOS设备可以与Safari存储的钥匙串项交互，以使用SecRequestSharedWebCredential和SecAddSharedWebCredential API进行密码自动填充。这些API只能在用户首次解锁设备并同意授权后才能使用。
    ...
    最后，iOS设备还支持HomeKit、HealthKit、Apple Watch等配件，以及AirDrop等安全性功能，以提供更加全面的安全保护。
    总之，iOS设备在访问Safari已存储的密码时，采用了一系列安全技术规格和功能，以保护用户数据和设备安全。

*   问题二：iOS有哪些密钥包？
    *   __外挂知识库前的回答:__ 
    在 iOS 中，有一些内置的密钥包可以用于加密和解密数据。这些密钥包包括：
    加密算法密钥包：用于加密和解密使用加密算法（如 AES）加密的数据。
    哈希算法密钥包：用于加密和解密使用哈希算法（如 SHA-256）加密的数据。
    随机数密钥包：用于生成随机数，用于加密和解密数据。
    此外，在 iOS 中还有一些第三方库可以使用，例如 OpenSSL 库和 NaCl 库等。这些库也可以用于加密和解密数据。
    总的来说，在 iOS 中，有一些内置的密钥包可以用于加密和解密数据，并且也可以使用第三方库。
    *   __外挂知识库后的回答:__ 
    iOS设备有四种密钥包，分别是系统密钥包、备份密钥包、托管密钥包和管理密钥包。系统密钥包用于设备常规操作中使用的封装类密钥的储存位置，备份密钥包在iTunes进行加密备份时创建，托管密钥包用于iTunes同步和MDM，和管理密钥包用于管理设备的MDM服务器上。这些密钥包都有不同的用途和保护级别，用户需要根据实际情况选择合适的密钥包。

可以看到，外挂知识库前，模型的回答更偏向于泛泛而谈，回答的内容缺乏具体的内容，而外挂知识库后，则能根据文档来做出较为精准正确的回答。


#### 性能

由于外挂知识库需要多常驻一个嵌入模型（本实验是m3e）因此相对未挂载知识库的版本会需要更多的显存资源。具体如下

*   外挂知识库前


![](data:image/webp;base64,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)


*   外挂知识库后

![](data:image/webp;base64,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)

### 实验完整代码

#### 实现代码1

共一个脚本，这个脚本集成了创建数据库，聊天的所有功能

`test.py`

```python
from transformers import AutoModel, AutoTokenizer
import glob
import chromadb
from sentence_transformers import SentenceTransformer

def get_vectordb():
    model = SentenceTransformer('/home/cjz/models/m3e-large')
    client = chromadb.Client()
    texts = []
    for filename in glob.glob("../knowledge_docs/*.txt"):
        with open(filename, encoding='utf-8') as f:
            texts.append(f.read())
    embeddings = model.encode(texts).tolist()
    collection = client.get_or_create_collection("test_collection")
    ids = [f'id{x + 1}' for x in range(len(texts))]
    collection.add(ids=ids, embeddings=embeddings, documents=texts)
    return collection, model


def get_model():
    tokenizer = AutoTokenizer.from_pretrained("/home/cjz/llms/THUDM/chatglm3-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("/home/cjz/llms/THUDM/chatglm3-6b", trust_remote_code=True).half().cuda()
    model = model.eval()
    return tokenizer, model


def query_related(text: str, model: SentenceTransformer, coll):
    embedding = model.encode(text).tolist()
    result = coll.query(query_embeddings=embedding, n_results=1)['documents']
    return result[0][0]


tokenizer, model = get_model()
embeddings_db, embeddings_encoder = get_vectordb()

max_len = 8192

past_key_values, history = None, []

while True:
    query = input("\nEnter：")
    print("\nAnswer：", end="")
    current_length = 0
    related_text = query_related(query, embeddings_encoder, embeddings_db)
    knowledge_embedded_query = f"'''\n{related_text}\n''' \n请上文提取信息并且结合你自己的判断和推理回答下面这个问题：“{query}”，如果这个问题和给你的上下文完全无关的话，就忘记这些上下文信息，然后正常的回答问题"

    for response, history, past_key_values in model.stream_chat(tokenizer, knowledge_embedded_query, history=history, top_p=1,
                                                                temperature=0.01,
                                                                past_key_values=past_key_values,
                                                                return_past_key_values=True):
        print(response[current_length:], end="", flush=True)
        current_length = len(response)
    print("")
```

#### 实现代码2

共两个脚本，一个用于创建和持久化数据库，一个用于聊天

`create_embeddings_db.py`

```python
# coding: utf-8
import os
import glob
from typing import List
# import torch
from multiprocessing import Pool
from tqdm import tqdm
from langchain.document_loaders import (
    CSVLoader,EverNoteLoader,
    PDFMinerLoader,TextLoader,
    UnstructuredEmailLoader,UnstructuredEPubLoader,
    UnstructuredHTMLLoader,UnstructuredMarkdownLoader,
    UnstructuredODTLoader,UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader, UnstructuredExcelLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document

source_directory = "../knowledge_docs"
embeddings_model_name = '/home/cjz/models/m3e-large'
chunk_size = 200
chunk_overlap = 20
output_dir = "./db"
k = 3


# Custom document loaders 自定义文档加载
class MyElmLoader(UnstructuredEmailLoader):
    def load(self) -> List[Document]:
        """Wrapper adding fallback for elm without html"""
        try:
            try:
                doc = UnstructuredEmailLoader.load(self)
            except ValueError as e:
                if 'text/html content not found in email' in str(e):
                    # Try plain text
                    self.unstructured_kwargs["content_source"]="text/plain"
                    doc = UnstructuredEmailLoader.load(self)
                else:
                    raise
        except Exception as e:
            # Add file_path to exception message
            raise type(e)(f"{self.file_path}: {e}") from e

        return doc


# Map file extensions to document loaders and their arguments
LOADER_MAPPING = {
    ".csv": (CSVLoader, {}),".doc": (UnstructuredWordDocumentLoader, {}),".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),".eml": (MyElmLoader, {}),".epub": (UnstructuredEPubLoader, {}),".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),".odt": (UnstructuredODTLoader, {}),".pdf": (PDFMinerLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),".pptx": (UnstructuredPowerPointLoader, {}),".txt": (TextLoader, {"encoding": "utf8"}),
    ".xls": (UnstructuredExcelLoader, {}),".xlsx": (UnstructuredExcelLoader, {}),
}

def load_single_document(file_path: str) -> List[Document]:
    ext = "." + file_path.rsplit(".", 1)[-1]
    if ext in LOADER_MAPPING:
        loader_class, loader_args = LOADER_MAPPING[ext]
        loader = loader_class(file_path, **loader_args)
        return loader.load()

    raise ValueError(f"Unsupported file extension '{ext}'")

def load_documents(source_dir: str, ignored_files: None) -> List[Document]:
    """
    Loads all documents from the source documents directory, ignoring specified files
    """
    ignored_files = [] if ignored_files is None else ignored_files
    all_files = []
    for ext in LOADER_MAPPING:
        all_files.extend(
            glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
        )
    filtered_files = [file_path for file_path in all_files if file_path not in ignored_files]

    with Pool(processes=os.cpu_count()) as pool:
        results = []
        with tqdm(total=len(filtered_files), desc='Loading new documents', ncols=80) as pbar:
            for i, docs in enumerate(pool.imap_unordered(load_single_document, filtered_files)):
                results.extend(docs)
                pbar.update()

    return results

def process_documents(ignored_files: List[str] = None) -> List[Document]:
    """
    Load documents and split in chunks
    """
    ignored_files = [] if ignored_files is None else ignored_files
    print(f"Loading documents from {source_directory}")
    documents = load_documents(source_directory, ignored_files)

    if not documents:
        print("No new documents to load")
        exit(0)
    print(f"Loaded {len(documents)} new documents from {source_directory}")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
    return texts

def main():
    # Create embeddings
    # print(torch.cuda.is_available())
    # Create and store locally vectorstore
    print("Creating new vectorstore")
    texts = process_documents()
    print(f"Creating embeddings. May take some minutes...")
    embedding_function = SentenceTransformerEmbeddings(model_name=embeddings_model_name)
    db = Chroma.from_documents(texts, embedding_function, persist_directory=output_dir)
    db.persist()
    print("Done")
if __name__ == "__main__":
    main()
```


`chat.py`

```python
import os
from transformers import AutoTokenizer, AutoModel
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

source_directory = "../knowledge_docs"
embeddings_model_name = '/home/cjz/models/m3e-large'
chunk_size = 200
chunk_overlap = 20
output_dir = "./db"
MODEL_PATH = os.environ.get('MODEL_PATH', "/home/cjz/llms/THUDM/chatglm3-6b")
TOKENIZER_PATH = os.environ.get("TOKENIZER_PATH", MODEL_PATH)

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()



def main():
    past_key_values, history = None, []
    embedding_function = SentenceTransformerEmbeddings(model_name=embeddings_model_name)
    db = Chroma(persist_directory=output_dir, embedding_function=embedding_function)


    while True:
        query = input("\nEnter：")

        response = db.similarity_search(query, k=3)
        relevant_information = ''.join(str([document.page_content for document in response]))
        knowledge_embedded_query = f"'''\n{relevant_information}\n''' \n请上文提取信息并且结合你自己的判断和推理回答下面这个问题：“{query}”，如果这个问题和给你的上下文并没有明显的关系，就忘记这些上下文信息，然后正常的回答问题"

        print("\nAnswer：", end="")
        current_length = 0
        for response, history, past_key_values in model.stream_chat(tokenizer, knowledge_embedded_query, history=history, top_p=1,
                                                                    temperature=0.01,
                                                                    past_key_values=past_key_values,
                                                                    return_past_key_values=True):
            print(response[current_length:], end="", flush=True)
            current_length = len(response)
        print("")


if __name__ == "__main__":
    main()
```