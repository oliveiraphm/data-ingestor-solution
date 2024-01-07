import streamlit as st
from aws.client import S3Client
from datasource.csv import CSVCollector
from contracts.catalogo import Catalogo

st.title("Essa é uma página de portal de dados")


#if st.button("Say hello"):
#    st.write("Why hello there")

aws_instancia = S3Client()
catalogo_de_produto = CSVCollector(Catalogo, aws_instancia, "C12:I209")
catalogo_de_produto.start()