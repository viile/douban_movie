# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
	screenwriter = scrapy.Field()
	starring = scrapy.Field()
	types = scrapy.Field()
	regions = scrapy.Field()
	language = scrapy.Field()
	releaseDate = scrapy.Field()
	length = scrapy.Field()
	alias = scrapy.Field()
	imdb = scrapy.Field()
	rating = scrapy.Field()
	ratingNum = scrapy.Field()
	commentaryNum = scrapy.Field()
	problemNum = scrapy.Field()
	filmCriticNum = scrapy.Field()
	recommendations = scrapy.Field()

