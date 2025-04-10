from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '朝闻天下'
    site_title = '朝闻天下 管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
