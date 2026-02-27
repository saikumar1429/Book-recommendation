import streamlit as st
import pandas as pd
import pickle

books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity (1).pkl', 'rb'))
if isinstance(books, dict): books = pd.DataFrame(books)

st.title("📚 Book Recommender Application")

def recommend(book):
    idx = books[books.title == book].index[0]
    scores = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)[1:6]
    return [books.iloc[i[0]].title for i in scores]

book = st.selectbox("Select a book to find similar books:", books.title.values)

if st.button("Recommend"):
    for i, b in enumerate(recommend(book), 1):
        st.write(f"{i}. **{b}**")
