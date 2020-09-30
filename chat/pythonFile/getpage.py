import re


def read_page():
        pass

css_file = []
js_file = []


def retutn_page():
    with open('../page/index.html', 'r', encoding='utf-8') as file_html:
        file = file_html.readline()
        while file:
            add_file_css = re.findall(r"<link.*?>", file)
            add_file_js = re.findall(r"<script.*?>", file)

            if len(add_file_css) > 0:
                css_file.append(add_file_css)
            elif len(add_file_js) > 0:
                js_file.append(add_file_js)

            file = file_html.readline()



retutn_page()



rest = re.findall(r"href=[\'|\"]([\w|\W]*\.css)", css_file[0][0])

res = re.findall(r'src=[\'|\"]([\W|\w]*\.js)', js_file[0][0])
print(rest)

print(res)

