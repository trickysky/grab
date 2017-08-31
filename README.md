# grab
### 基于Scrapy开发的爬虫项目, 目前包含以下爬虫

- 单车数据
    - [ ] 摩拜单车
    - [ ] OFO

- 交通数据
    - [ ] 四维交通数据

### 注意事项

- 对 project 的 templates 软链接至 Scrapy 的默认 templates 路径
    ```
    ln -s {PATH}/grab/templates {PATH}/lib/python2.7/site-packages/scrapy
    ```

- 设置全局的 python 路径
    ```
    vim {PATH}/lib/python2.7/site-packages/custom.pth
    ```
    添加 `{PATH}/grab`

