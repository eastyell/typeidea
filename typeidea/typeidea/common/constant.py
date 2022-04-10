# Define some constants

STATUS_DELETE = 0
STATUS_NORMAL = 1
STATUS_DRAFT = 2

STATUS_HIDE = 0
STATUS_SHOW = 1

STATUS_ITEMS = (
    (STATUS_NORMAL, '正常'),
    (STATUS_DELETE, '删除'),
)

STATUS_ITEMS_POST = (
    (STATUS_NORMAL, '正常'),
    (STATUS_DELETE, '删除'),
    (STATUS_DRAFT, '草稿')
)

STATUS_ITEM_SIDE = (
    (STATUS_SHOW, '展示'),
    (STATUS_HIDE, '隐藏'),
)

SIDE_TYPE = (
    (1, 'HTML'),
    (2, '最新文章'),
    (3, '最热文章'),
    (4, '最新评论'),
)