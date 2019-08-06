from django.utils.safestring import mark_safe
class Pagination:

    def __init__(self,page_num,all_count,per_num,max_show):
        try:
            page_num = int(page_num)
        except Exception as e:
            page_num=1
        self.page_num=page_num
        self.all_count=all_count
        self.per_num=per_num
        self.max_show=max_show

    def start(self):
        return (self.page_num-1)*self.per_num
    def end(self):
        return self.page_num*self.per_num

    def page_html(self):
        half_show=self.max_show//2
        total_num,more =divmod(self.all_count,self.per_num)
        if more:
            total_num+=1

        if total_num < self.max_show:
            page_start =1
            page_end =total_num
        else:
            if self.page_num < half_show:
                page_start = 1
                page_end=self.page_num + half_show
            elif self.page_num + half_show > total_num:
                page_start=self.page_num-half_show
                page_end=total_num
            else:
                page_start = self.page_num - half_show
                page_end = self.page_num + half_show

        page_list=[]
        for i in range(page_start,page_end+1):
            if  i == self.page_num:
                page_list.append("<li class='active'><a  href='?page={}'>{}</a></li>".format(i,i))
            else:
                page_list.append("<li><a  href='?page={}'>{}</a></li>".format(i, i))

        page_html=''.join(page_list)
        print(page_html)
        return mark_safe(page_html)