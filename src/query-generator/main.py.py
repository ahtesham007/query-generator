from datetime import datetime

class Generate:

	def to_sql(self,data,table_name:str) -> bool:

		try:
			
			col_list_length = len(data.columns)
			insert_query = 'INSERT INTO '+table_name
			column_str = ' ('
			for i,col in enumerate(data.columns):
				if i == col_list_length -1:
					column_str += '`'+col+'`)'
				else:
					column_str += '`'+col+'`,'

			insert_query += column_str +' VALUES'

			data_len = len(data)
			for ind,row in enumerate(data.itertuples()):
				batch_query = ' ('
				for index in range(col_list_length):
					value = str(row[index+1])
					if index != col_list_length - 1:
						batch_query += "'"+value+"',"
					else:
						batch_query += "'"+value+"'"
				if ind != data_len - 1:
					batch_query += '),'
				else:
					batch_query += ');'
				insert_query+=batch_query

			return insert_query

		except Exception as e:
			print(f'{datetime.now()} Error while generating insert query :: {e}')
			return ""
