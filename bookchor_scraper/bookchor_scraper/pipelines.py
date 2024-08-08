# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookchorScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        #fix rating
        val = adapter.get('rating') #["fill", "fill", "fill", "fill", "without-fill"]
        adapter['rating'] = self.convertToNum(val)

        return item

    def convertToNum(self, ls):
        # ["fill", "fill", "fill", "fill", "without-fill"]
        starCounter = 0

        star_val = {
            "fill" : 1,
            "half" : 0.5,
            "without-fill": 0
        }

        for item in ls:
            starCounter += star_val.get(item)

        return starCounter


