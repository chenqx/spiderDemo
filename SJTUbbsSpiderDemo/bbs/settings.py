# -*- coding: utf-8 -*-

# Scrapy settings for bbs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbs'

CONCURRENT_REQUESTS = 200
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = True
RETRY_ENABLED = True


SPIDER_MODULES = ['bbs.spiders']
NEWSPIDER_MODULE = 'bbs.spiders'

# JOBDIR = 'jobdir'
ITEM_PIPELINES = {
    'bbs.pipelines.XmlWritePipeline': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbs (+http://www.yourdomain.com)'
