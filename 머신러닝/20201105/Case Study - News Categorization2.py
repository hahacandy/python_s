from sklearn.feature_extraction.text import  CountVectorizer

# 텍스트의 벡터값을 구하는 모듈은 이미 만들어져있다

vectorizer = CountVectorizer()
corpus = [
    'This is the first document test test test.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?'
]

corpus2 = [
    'This is the first document test test test.',
    'my name is',
]

X = vectorizer.fit_transform(corpus)
print(X.toarray())
print()

X = vectorizer.fit_transform(corpus2)
print(X.toarray())

# corpus, corpus2 의 값을 비교했을때 0은 그냥 빈공간을 의미하는거같은데 잘은 몰겟다

print(vectorizer.get_feature_names())
