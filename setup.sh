mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"1162100124@stu.hit.edu.cn\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml