import logging.config
import math
import os
import random
import re
import hashlib

from setup import LOG_CONFIG, RE_PATTERNS

logging.config.dictConfig(LOG_CONFIG)
_logger = logging.getLogger('myctftools')


def split(file_path: str, chunk_size: str, output_directory: str, shuffle=False):
    """
    日期：2020-12-06
    功能：将指定的文件按分割块的大小进行等分
    :param file_path:  待分割文件的路径
    :param chunk_size:  指定分隔块大小，默认为单位为字节，可以用如下格式输出：1M、1K等，1M=1024K
    :param output_directory:  分割后文件输入的目录，默认为格式为 xxx.zip.001
    :param shuffle:  是否乱序输出
    :return: 在输出目录中，会生成md5的校验文件
    """
    # 判断输入的参数是否正确
    if not chunk_size.startswith('0') and re.match(RE_PATTERNS['chunk_size'], chunk_size) \
            and os.path.exists(file_path):
        # 将块大小转换为字节并获得输出文件个数
        chunk_size = chunk_size.lower()
        if chunk_size.endswith('k'):
            chunk_size_in_bytes = int(chunk_size[:-1]) * math.pow(1024, 1)
        elif chunk_size.endswith('m'):
            chunk_size_in_bytes = int(chunk_size[:-1]) * math.pow(1024, 2)
        else:
            chunk_size_in_bytes = int(chunk_size)
        file_size = os.path.getsize(file_path)
        output_file_num = math.ceil(float(file_size)/chunk_size_in_bytes)
        # 生成乱序后缀
        output_file_suffixes = list(range(output_file_num))
        if shuffle:
            random.shuffle(output_file_suffixes)
        print(output_file_suffixes)
        # 判断输出目录是否存在，不存在则默认与输入文件同目录
        if not os.path.exists(output_directory):
            output_directory = os.path.abspath(os.path.join(file_path, '../out'))
            if not os.path.exists(output_directory):
                os.mkdir(output_directory)
        # 为源文件计算md5值
        md5_algorithm = hashlib.md5()
        # 开始读取并输出文件
        _logger.info('文件：{}，将被拆分为：{}个子文件，每个文件块大小为（最后一个除外）：{}'
                     .format(os.path.basename(file_path), output_file_num, chunk_size))
        with open(file_path, mode='rb') as input_file:
            for output_file_suffix in output_file_suffixes:
                output_file_path = os.path.join(output_directory, os.path.basename(file_path) + str(output_file_suffix))
                output_file = open(output_file_path, mode='wb')
                chunk = input_file.read(chunk_size_in_bytes)
                md5_algorithm.update(chunk)
                output_file.write(chunk)
                output_file.flush()
                output_file.close()
                _logger.info('子文件：{}，写入完成'.format(os.path.basename(output_file_path)))
            input_file.close()
            _logger.info('文件：{}拆分完成'.format(os.path.basename(file_path)))
            # 将源文件的md5值写入文件，供后期合并时校验
            md5_file_path = os.path.join(output_directory, os.path.basename(file_path) + '_md5.txt')
            md5_file = open(md5_file_path, mode='w', encoding='utf-8')
            md5_file.write(md5_algorithm.hexdigest())
            md5_file.flush()
            md5_file.close()
            _logger.info('检验文件：{}，写入完成'.format(os.path.basename(md5_file_path)))
    else:
        _logger.error('参数输入错误，请重新输入！')


def combine(input_directory: str, output_directory: str, is_shuffled=False, **kwargs):
    """
    日期：2020-12-06
    功能：将目录中待合并的文件按照文件名的升序进行合并。若不确定合并前的文件是按照文件名的顺序拆分的，
          程序会穷举所有可能的文件合并顺序。在这种模式下，若提供了源文件的md5校验值，程序则会验证合并是否成功。
    :param input_directory: 待合并文件所在的目录，请确保文件夹内只有待合并的文件
    :param output_directory: 合并后文件输出的目录，默认输出至输入目录下的out文件夹
    :param is_shuffled: 穷举文件合并所有可能
    :param kwargs: md5_file_path, md5文件路径
    :return:
    """
    # 判断


if __name__ == '__main__':
    split('../workfile', '5', 'asdf', True)
