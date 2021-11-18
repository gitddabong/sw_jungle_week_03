#-*- coding:utf-8 -*-
import os 
def generate_folders(problems_str):
    '''generate_folder.py파일이 있는 위치에 백준코딩 문제 폴더 생성 함수 
    
    Args: 
        problems_str (str): whitespace로 구분된 백준 문제 번호 스트링
    Returns:
        None
    '''
    problems_list = problems_str.split()
    path_root = os.getcwd()
    for num in problems_list:
        os.mkdir(os.path.join(path_root, num))


if __name__ == '__main__':
    problems_str = '''1991
5639
1197
1260
11724
2606
11725
1707
21606
14888
2573
2617
2178
18352
1916
2665
7569
3055
2294
2252
2637
1432
1948
'''
    generate_folders(problems_str)
