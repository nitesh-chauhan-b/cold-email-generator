# text ="""<div class="ibm--card__copy__inner">Professional<br/>GUADALAJARA, MX</div>"""
# list = text.split("<br/>")
# print(list)
# print(list[0].find(">"))
# _,_,res = list[0].partition(">")
# res,_,_ = list[1].partition("<")
# print(res)

test = """
            Bangalore, IN, 560103
            
        """
list = test.strip()
# list = list[0][-1]

print(list)