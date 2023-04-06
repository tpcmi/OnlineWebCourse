# 过程记录

## 第十章

### 10-5-6

- 修改models后，如果删除了migrations文件夹里的数据，再进行`makemigrations`
  的操作，会导致修改不生效的现象，因为在数据库表里`django_migrations`已经
  记录了之前的整数递增记名，如0001、0002...此时进行`migrate`会被认为已应用，因此不会对修改生效
- 在设计models时，适当增加一些冗余的字段，可以减少查询的过程中多表的联结查询（如：Course表中，
  增加的course_org字段）
- 当A是B的外键时，在A中可以通过`b_set()`的形式，反向取出b的值，其主要作用是避免
  在A中查询B的值时可能造成的循环`import`（or 在局部作用域内import可以避免循环引用）
- 分页使用了django-pure-pagination库，采用`XXX.object_list`读取数据

### 10-7-8


