# PaddleSpeech 记录

## 介绍

PaddleSpeech是百度PaddlePaddle开源深度学习平台的其中一个项目，是基于飞桨 PaddlePaddle 语音方向的开源模型库，用于语音和音频中的各种关键任务的开发，包含大量可以直接下载使用的基于深度学习前沿和有影响力的预训练模型。
这个文档主要分为两个部分：

* 安装
    * 正常安装流程
    * 安装过程中可能遇到的问题

* 使用例子
    * 一个最简单的例子
    * 一个比较实用的例子
    * 客户端和服务端的流式服务例子

## 环境安装流程（gpu）

这部分的一小节首先会介绍一下正常的安装流程，第二小节是我在安装paddlespeech时候遇到的各种问题。

### 正常情况下的安装流程

要安装两个东西，一个是paddlepaddle，这个是主框架，是基础的东西。另外一个是paddlespeech，可理解为这个基础之上的拓展。

下面的代码是paddlespeech的python demo代码，用于留在最后验证整套东西有没有安装好


```python
from paddlespeech.cli.asr.infer import ASRExecutor
asr = ASRExecutor()
result = asr(audio_file="zh.wav",model='conformer_wenetspeech')
print(result)
```

#### 第一步、安装paddlepaddle-gpu

可以根据 [官网上的指引 ](https://www.paddlepaddle.org.cn/) 安装对应的paddlepaddle-gpu版本，但是如果用于使用paddlespeech的话，从经验来看，使用最新的版本并不是一个很好的选择，可以在官网找到旧版本。 （后面会介绍原因）。

```bash
pip install paddlepaddle-gpu==2.4.2
```

安装完成后检验的python脚本如下:

```python
>>> import paddle
>>> paddle.utils.run_check()
```

只有这两个语句都没问题才算装好了，才可以进入下一步。


#### 第二步、安装paddlespeech

在安装之前首先得确保paddlepaddle已经没问题了。至于这个直接pip安装就可以了，貌似不需要和paddlepaddle进行严格的版本搭配，装最新的就可以了。

```bash
pip install paddlespeech
```

## PaddleSpech环境安装遇到的问题

下面是遇到的这些问题当时的一些系统信息：

* CUDA版本12.1
* cuDNN Version: 8.9
* Python版本3.9

### 第一个问题

#### 问题

安装完paddlepaddle-gpu之后，import paddle可能会发生下面这个错误。它的报错信息长这样

```bash
/usr/local/lib64/libstdc++.so.6: version 'GLIBCXX_3.4.30' not found (required by /lib/x86_64-linux-gnu/libicuuc.so.70)
```

意思就是这个库里面的'GLIBCXX_3.4.30'因为某种原因找不到

#### 解决

用下面这个命令详细看看这个文件

```shell
ll /usr/local/lib64/libstdc++.so.6
```
发现这个libstdc++.so.6是一个软链接，指向同目录下的一个库文件


使用下面这个命令大致查看一下当前的这个库libstdc++.so.6支持（或者说包含）的GLIBCXX信息

```shell
strings /usr/local/lib64/libstdc++.so.6 | grep GLIBCXX
```
结果不意外的发现最多只有GLIBCXX_3.4.29，没有我们需要的GLIBCXX_3.4.30的信息

用下面的这个指令来找一下系统中还有哪些libstdc++.so.6，它们也许会包含GLIBCXX_3.4.30。

```shell
locate libstdc++.so.6
```
会看到系统中有很多libstdc++.so.6
还是用上面的那个strings命令从这一大堆libstdc++.so.6中找到有包含GLIBCXX_3.4.30的那个libstdc++.so.6，然后记一下它的目录
这个时候我们理论上只要把出错的 /usr/local/lib64/libstdc++.so.6这个软链接指向我们刚找到的那个有GLIBCXX_3.4.30的那个新libstdc++.so.6就可以
但是由于/usr/local/lib64/libstdc++.so.6这个软链接只有root才能修改，由于一般情况下没有root，因此直接改软链接是不行的。这个时候可以修改下面这个环境变量，把我们的刚刚找到的那个新libstdc++.so.6的所在目录设置为环境变量LD_LIBRARY_PATH的值。

```shell
export LD_LIBRARY_PATH= path/to/the/new/lib/dir$LD_LIBRARY_PATH
```

然后这个问题就会解决了

### 第二个问题

#### 问题
成功安装完padlepadle，再安装完padlespeech之后，运行demo代码的时候会出现这个错误

```bash
AttributeError: module 'numpy' has no attribute 'complex'
```

#### 解决

这个问题的原因是padelspeech一起自动安装的librosa版本太老了，还没对numpy新版本的变化进行适配。这个时候直接单独重新安装新版本librosa之后可以了。命令如下


```shell
pip uninstall librosa
pip install librosa==0.10.0
```

### 第三个问题

## 问题

用padelpadel-gpu 2.6.1的情况下（在解决完上述的第一个和第二个问题之后）运行demo代码会出现下面的这个错误

```shell
(paddle_test_4) [cjz@yaai paddle_helloworld]$ python test.py
W0416 11:36:12.186519 30662 gpu_resources.cc:119] Please NOTE: device: 0, GPU Compute Capability: 8.9, Driver API Version: 12.2, Runtime API Version: 12.0
W0416 11:36:12.187281 30662 gpu_resources.cc:164] device: 0, cuDNN Version: 8.9.
2024-04-16 11:36:12.506 | INFO     | paddlespeech.s2t.modules.embedding:__init__:150 - max len: 5000
[2024-04-16 11:36:13,579] [   ERROR] - list index out of range
Traceback (most recent call last):
  File 
............
"/home/cjz/anaconda3/envs/paddle_test_4/lib/python3.9/site-packages/paddlespeech/cli/asr/infer.py", line 335, in postprocess
    return self._outputs["result"]
KeyError: 'result'
```

## 解决


这个keyError尚不知道是如何产生的，根据GitHub的讨论，这应该是一个Bug，可以理解为最新版的paddlespeech(1.4.1)尚未支持一些新版paddlepaddle-gpu(2.6.1)的改变。 网上的方法指示要安装较旧的paddlepaddle版本解决，也有很多其他的解决方法（比如修改内部的源码，但这个比较复杂）。都进行尝试之后发现只有降级能快速解决问题，我这里是把2.6.1的paddlepaddle-gpu换成 2.5.2，命令如下


```shell
Pip uninstall paddlepaddle
Pip install paddlepaddle-gpu==2.5.2
```


注：一开始我尝试降级到2.4.2，但这个版本的paddlepaddle-gpu无法和当前系统的Cuda 12.1共用，会报如下错

```shell
libcudart.so.10.2: cannot open shared object file: No such file or directory
```

这是因为Cuda 12.1 已经没有这个libcudart.so.10.2了，后来尝试降级到2.5.2便成功了。

## PaddleSpech的使用（音频生成文字、Python API）

### 一个极简的例子

```python
import paddle
from paddlespeech.cli.asr import ASRExecutor

asr_executor = ASRExecutor()
text = asr_executor(
    model='conformer_wenetspeech',
    lang='zh',
    sample_rate=16000,
    config=None,  # Set `config` and `ckpt_path` to None to use pretrained model.
    ckpt_path=None,
    audio_file='./zh.wav',
    force_yes=False,
    device=paddle.get_device())
print('ASR Result: \n{}'.format(text))
```

* input(必须输入)：用于识别的音频文件。
* model：ASR 任务的模型，默认值：conformer_wenetspeech。
* lang：模型语言，默认值：zh。
* codeswitch: 是否使用语言转换，默认值：False。
* sample_rate：音频采样率，默认值：16000。
* config：ASR 任务的参数文件，若不设置则使用预训练模型中的默认配置，默认值：None。
* ckpt_path：模型参数文件，若不设置则下载预训练模型使用，默认值：None。
* force_yes；不需要设置额外的参数，一旦设置了该参数，说明你默认同意程序的所有请求，其中包括自动转换输入音频的采样率。默认值：False。
* device：执行预测的设备，默认值：当前系统下 paddlepaddle 的默认 device。
* verbose: 如果使用，显示 logger 信息。


注：这个[页面](https://gitcode.com/PaddlePaddle/PaddleSpeech/blob/develop/paddlespeech/resource/pretrained_models.py)列出了所有可以直接调用的预训练模型列表(里面也包含了每个模型的一些信息)，使用时可以将模型名字传入model参数位置

### 一个更进一步的例子

在现实情况下，经常需要给模型喂一些长音频进行推理，但是直接喂是不行的，因为会报错

```shell
[ ERROR] - Please input audio file less then 50 seconds.
```

这个时候，需要吧音频切成一块一块小于五十秒的，可以使用auditok库来对音频进行智能切分（也就是根据响度和连续性来在某些合适的地方断开音频，拆分成片段）

下面是代码部分，首先是最重要的auditok智能分割器的定义

```python
audio_regions = auditok.split(
        path,
        min_dur=min_dur,  
        max_dur=max_dur,  
        max_silence=max_silence,    
        energy_threshold=energy_threshold 
    )
```

这些参数的含义：
* min_dur 单位是秒，指的是最小能接受的智能切割的片段长度
* max_dur 单位是秒，指的是最大能接受的智能切割的片段长度
* max_silence 会被判定为对话间隔的沉默的最大时长阈值
* energy_threshold 会被分析的音频响度门限

定义完切割器之后就可以开始切割，结构化保存，代码如下：

```python
dir_name = f"split_wav_{time.strftime('%Y-%m-%d-%H:%M', time.localtime())}"
    for serial_number, audio_region in enumerate(audio_regions):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        file_name = ('000000' + str(serial_number))[-5:]
        file_save = os.path.join(dir_name, file_name + '.wav')
        _ = audio_region.save(file_save)

    print(f"segment_finished, path:{dir_name}")
    return dir_name
```

运行结束之后会得到这样的文件结构

```bash
├── split_wav_2024-04-23-14:31
│   ├── 00000.wav
│   ├── 00001.wav
│   └── 00002.wav
```

接下来一步就是轮流对每一个片段进行音频转文字，这部分的代码和例子一是差不多的，如下

```python
def audio_to_txt(seg_dir):
    asr_executor = ASRExecutor()

    audio_seg_list = os.listdir(seg_dir)
    # 排序一下，确保是正确的的顺序，等下要拼接起来
    audio_seg_list.sort(key=lambda x: int(os.path.splitext(x)[0]))
    words = []
    for file in audio_seg_list:
        text = asr_executor(
            model='conformer_wenetspeech',
            lang='zh',
            sample_rate=16000,
            config=None,
            ckpt_path=None,
            audio_file=seg_dir + '/' + file,
            device=paddle.get_device(), force_yes=True)
        words.append(text)
    return words
```

使用这段代码生成的一个文本例子如下：

_隆东时节在重庆市乌山县竹贤乡下庄村黄灯灯的柑橘挂满之头夏庄村党支部书记毛香林忙着组织村民进行采摘让柑橘沿着村庄四周峭壁上蜿蜒曲折的山路运出去增加村民的收入山凿一尺宽一尺路修一丈长一丈就算我们这代人穷十年苦十年也一定要让夏辈人过上好日子二零二一年二月二十五日在全国脱贫攻坚总结表彰大会上习近平总书记转引毛香林说给乡亲们的这句话点赞这种自立自强苦干时干用自己的双手创造幸福生活的奋进精神曾经的夏庄村出行只能徒步翻越绝壁',_


用PaddleSpeech的TexeExecuter可以在一定程度上修正文本的符号，代码比较简单，如下：

```python
def optimize_text(texts):
    text_executor = TextExecutor()
    result = text_executor(
        text=str(texts),
        task='punc',
        model='ernie_linear_p3_wudao',
        device=paddle.get_device(),
    )
    return result
```

修正之后差不多是这样的：

_隆东时节，在重庆市乌山县竹贤乡下庄村黄灯灯的柑橘挂满之头，夏庄村党支部书记毛香林忙着组织村民进行采摘，让柑橘沿着村庄四周峭壁上蜿蜒曲折的山路运出去，增加村民的收入，山凿一尺宽一尺，路修一丈长一丈，就算我们这代人穷十年苦十年，也一定要让夏辈人过上好日子。二零二一年二月二十五日，在全国脱贫攻坚总结表彰大会上，习近平总书记转引毛香林说给乡亲们的这句话，点赞这种自立自强，苦干时干，用自己的双手创造幸福生活的奋进精神。曾经的夏庄村，出行只能徒步翻越绝壁。_

这里是第二个例子的全部代码：

```python
import auditok
import os
import paddle
from paddlespeech.cli.asr import ASRExecutor
from paddlespeech.cli.text import  TextExecutor
import time

def segment_audio(path, min_dur=1, max_dur=50, max_silence=1, energy_threshold=55):

    audio_regions = auditok.split(
        path,
        min_dur=min_dur,  # 单位是秒，指的是最小能接受的智能切割的片段长度
        max_dur=max_dur,  # 单位是秒，指的是最大能接受的智能切割的片段长度
        max_silence=max_silence,     # 会被判定为对话间隔的沉默的最大时长阈值
        energy_threshold=energy_threshold  # 会被分析的音频响度门限
    )
    dir_name = f"split_wav_{time.strftime('%Y-%m-%d-%H:%M', time.localtime())}"
    for serial_number, audio_region in enumerate(audio_regions):

        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # 下面这行代码的意思是补全成00001,00002这样的文件名，等下要拿来排序
        file_name = ('000000' + str(serial_number))[-5:]
        file_save = os.path.join(dir_name, file_name + '.wav')
        _ = audio_region.save(file_save)

    print(f"segment_finished, path:{dir_name}")
    return dir_name

def audio_to_txt(seg_dir):
    asr_executor = ASRExecutor()

    audio_seg_list = os.listdir(seg_dir)
    # 排序一下，确保是正确的的顺序，等下要拼接起来
    audio_seg_list.sort(key=lambda x: int(os.path.splitext(x)[0]))
    words = []
    for file in audio_seg_list:
        text = asr_executor(
            model='conformer_wenetspeech',
            lang='zh',
            sample_rate=16000,
            config=None,
            ckpt_path=None,
            audio_file=seg_dir + '/' + file,
            device=paddle.get_device(), force_yes=True)
        words.append(text)
    return words


def optimize_text(texts):
    text_executor = TextExecutor()
    result = text_executor(
        text=str(texts),
        task='punc',
        model='ernie_linear_p3_wudao',
        device=paddle.get_device(),
    )
    return result

def main():
    # 切分音频为片段
    audio_segment_dir = segment_audio('test.wav')

    # 音频转换为文字
    texts = audio_to_txt(audio_segment_dir)
    print(str(texts))

    # 优化标点符号
    optimized_text = optimize_text(texts)
    print(optimized_text)

if __name__ == '__main__':
    main()
```

### 客户端和服务端的例子

Asr还可以用服务端客户端的形式来进行流式语音转文字，这里我们需要使用模型列表里带有’online’的模型。

3.1 第一步：准备两个文件

其一：这是一个配置ymal配置文件,他的模板在[这里](https://gitcode.com/PaddlePaddle/PaddleSpeech/blob/develop/demos/streaming_asr_server/conf/ws_conformer_wenetspeech_application_faster.yaml)
需要在这个模板文件里面配置包括但不限于模型名字、音频采样率、服务端需要被挂载的端口等内容

其二：一个log文件，内容为空就可以

这是服务端的代码，替换为刚刚那两个文件的路径：

```python
from paddlespeech.server.bin.paddlespeech_server import ServerExecutor

server_executor = ServerExecutor()
server_executor(
    config_file="./asr_conf.yaml",
    log_file="./paddlespeech.log")
```
然后开一个终端运行起来放一边。


接下来是客户端代码，这里端口要和服务端一样才可以

```python
from paddlespeech.server.bin.paddlespeech_client import ASROnlineClientExecutor

asrclient_executor = ASROnlineClientExecutor()
res = asrclient_executor(
    input="./zh.wav",
    server_ip="127.0.0.1",
    port=8091,
    sample_rate=16000,
    lang="zh_cn",
audio_format="wav")
print(res)
```

运行客户端代码就解决完毕了。
