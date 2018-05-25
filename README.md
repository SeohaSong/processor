# File Execution Order
 
```bash
python set-up.py
python main.py
```

## Output Pickle Files

```
./data/imdb_master_df
./data/preprocessed_df
./freq_dic
```

# Preprecess Discription

```python
text = re.sub(r"<br />", " ", text)
# 텍스트 사이에 마크업 삭제
text = re.sub(r'[^\w\']', ' ', text)
# {'} 빼고 모든 특수기호 제거
text = re.sub(r"\d+", "00", text)
# 숫자는 00으로 변경
text = re.sub(r"\s+", " ", text)
# 공백은 모두 1개의 띄어쓰기로
text = re.sub(r'^ ', '', text)
text = re.sub(r' $', '', text)
# 문장 앞뒤 공백 제거
text = text.lower()
# 소문자로 변환
```

2. 
