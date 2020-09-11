import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import json
import pandas as pd
import os
current_path = os.path.dirname(__file__)

#https://dashboard.heroku.com/apps/complexetworkbychen/deploy/heroku-git


page=st.sidebar.selectbox(
    "复杂网络系统",
    ["系统介绍","网络计算","系统接口"]
)

if page=="系统介绍":
    st.title("复杂网络系统Project")
    st.subheader('一、功能:')
    st.text('balabala')
    st.subheader('二、系统简介:')
    st.text('balabala')
    st.subheader('三、系统框架:')
    st.text('balabala')
    #st.map(part_df)似乎是用来地理绘图的 可能能用于复杂网络绘图
elif page=="网络计算":
    st.title("复杂网络系统")
    x=1
    y=2
    st.subheader('网络特征数值计算:')
    st.write('平均度分布：', x+y)
    st.write('图的直径：', x + y)
    st.write('平均最短路径：', x + y)
    st.write('集聚系数：', x + y)
    st.write('核数：', x + y)
    '''
    #右拉计算一些数值
    st.subheader('Clustering coefficient calculation:')
    x = st.slider('degree(u)',min_value=2)
    y= st.slider('T(u)',min_value=1)
    st.write(x,y, 'Clustering coefficient is', 2*y/(x*(x-1)))
    '''



    #画折线图
    st.subheader('relationship of A and B:')
    chart_data = pd.DataFrame(
        np.random.randn(20, 4),
        columns=['a', 'b', 'c','d'])
    st.line_chart(chart_data)

    #画棒状图
    st.subheader('node-degree distribution of X:')
    chart_data = pd.DataFrame(
        np.random.randn(50, 1),
        columns=['a'])
    st.bar_chart(chart_data)

    #显示matplotlib画的复杂网络图
    st.subheader('xx structure of X:')
    # H = nx.path_graph(10)
    # G.add_nodes_from(H)
    G = nx.Graph()
    nx.add_cycle(G, [0,1, 2, 3, 4])
    nx.draw(G, with_labels=True)
    #plt.hist(G, bins=20)
    st.pyplot()

    # 3d绘图 可以用gephi在外面画完把图插入进来
    st.subheader('3d 图:')

    #单节点属性查看
    st.subheader('属性:')

    #单节点和邻居的关系图显示
    st.subheader('图:')


    @st.cache #节省其包裹函数的调用
    def load_data():
        #print(current_path)
        with open(current_path+"/testdata-kouhong.json",encoding='utf-8') as data:
            df=json.load(data)
        #df = pd.read_json(current_path+"/testdata-kouhong.json",lines=True)#,orient="records"
        df = pd.DataFrame(df)
        df.columns = ['img', 'username', 'content','zf_num','review_num','praise_num']
        return df

    df=load_data()
    st.table(df.head())

    username_list = df["username"].unique()

    username_type = st.sidebar.selectbox(
        "Which kind of username do you want to explore?",
        username_list
    )

    content_list = df["content"].unique()

    content_name = st.sidebar.selectbox(
        "Which content?",
        content_list
    )

    part_df = df[(df["username"]==username_type)]# & (df['content']==content_type)
    st.write(f"根据你的筛选，数据包含{len(part_df)}行")

elif page == "系统接口":
    st.title("复杂网络系统")



