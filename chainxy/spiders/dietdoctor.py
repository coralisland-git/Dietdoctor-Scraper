# -*- coding: utf-8 -*-

import scrapy

import json

import os

import scrapy

from scrapy.spiders import Spider

from scrapy.http import FormRequest

from scrapy.http import Request

from chainxy.items import ChainItem

from lxml import etree

from lxml import html

import pdb

from scrapy import signals

from scrapy.xlib.pydispatch import dispatcher


class dietdoctor(scrapy.Spider):

	name = 'dietdoctor'

	domain = ''

	history = []

	res_data = []


	def __init__(self):

		dispatcher.connect(self.spider_closed, signals.spider_closed)

	def spider_closed(self, spider):

		try:

			publish = { 

				"Breakfast" : self.res_data 

			}

			with open('result.json', 'w') as outfile:

				json.dump(publish, outfile)

			print('************************ Success ***********************')

		except:

			pdb.set_trace()

	
	def start_requests(self):

		url  = 'https://www.dietdoctor.com/low-carb/keto/recipes/all'

		yield scrapy.Request(url=url, callback=self.parse) 


	def parse(self, response):

		product_list = response.xpath('//li[contains(@class, "preview-item orientation-horizontal")]//div[@class="inner"]/a/@href').extract()

		for product in product_list:

			yield scrapy.Request(product, callback=self.parse_detail)


	def parse_detail(self, response):

		try:

			name_item = ''.join(response.xpath('//h1[@id="huge-feature-box-title"]//text()').extract())

			ingredient_list = response.xpath('//ul[@class="ckdc-recipe-ingredients-list"]//li')

			ingre_parent_item = []

			recipe_item = ''

			for ingredient in ingredient_list:

				try:

					details = self.eliminate_space(ingredient.xpath('.//text()').extract())

					ingre_child_item = {}

					try:

						number = ingredient.xpath('.//span[@class="ingredient-value ingredient-value-us"]//@data-servings').extract_first()

						try:
							number = json.loads(number)['1']['value'].replace('<sub>', '').replace('<sup>', '').replace('</sup>', '').replace('</sub>', '')
						except:
							number = str(json.loads(number)['1']['value'])



						ingre_child_item = {

							"Ingredient" : details[-1],

							"Number" : number
						}

						recipe_item += number + ' ' + details[-1] + ', '


					except:

						ingre_child_item = {

							"Ingredient" : details[-1],

							"Number" : details[0]
						}

						recipe_item += details[0] + ' ' + details[-1] + ', '

					ingre_parent_item.append(ingre_child_item)

				except Exception as e:

					print('~~~~~~~~~~~~~~~~~', e)

					pdb.set_trace()

			nutrition_list = response.xpath('//div[@class="more-nutrients-content"]//div[contains(@class, "nutrient")]')

			nutrition_item = {

				"Net carbs" : ''.join(response.xpath('//div[@class="more-nutrients-content"]//div[@class="nutrient carbs"]//span[@class="nutrient-grams"]//text()').extract()), 

				"Fiber":''.join(response.xpath('//div[@class="more-nutrients-content"]//div[@class="nutrient fiber"]//span[@class="nutrient-grams"]//text()').extract()),

				"Fat": ''.join(response.xpath('//div[@class="more-nutrients-content"]//div[@class="nutrient fat"]//span[@class="nutrient-grams"]//text()').extract()),

				"Protein": ''.join(response.xpath('//div[@class="more-nutrients-content"]//div[@class="nutrient protein"]//span[@class="nutrient-grams"]//text()').extract()),

				"kcal": ''.join(response.xpath('//div[@class="more-nutrients-content"]//div[@class="nutrient kcal"]//span[@class="nutrient-grams"]//text()').extract())
			}

			instruction_parent_item = []

			instruction_list = response.xpath('//ol[@class="recipe-steps-list"]//li')

			ind = 0

			for instruction in instruction_list:

				instruction_parent_item.append({
						"step"+str(ind+1) : ''.join(instruction.xpath('.//text()').extract()).encode('ascii','ignore')
					})

			item = {

				"Name": name_item,

				"Ingredients": ingre_parent_item,

				"Nutrition": nutrition_item,

				"Recipe":recipe_item[:-2],

				"Instructions": instruction_parent_item
			}

			self.res_data.append(item)

		except:

			pdb.set_trace()


	def validate(self, item):

		try:

			return item.replace('\n', '').replace('\t','').replace('\r', '').strip()

		except:

			pass

	def eliminate_space(self, items):
		tmp = []
		for item in items:
			if self.validate(item) != '':
				tmp.append(self.validate(item))
		return tmp