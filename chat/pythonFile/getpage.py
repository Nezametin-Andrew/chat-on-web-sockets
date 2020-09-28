
def return_page(self):
    with open('../page/index.html', 'r', encoding='utf-8') as f_page:
        with open('../page/style.css', 'r', encoding='utf-8') as s_page:
            page_html = f_page.readlines()
            style_page = s_page.read()
            page_html[5] = f'<style>{style_page}</style>'
            return 'hello'
