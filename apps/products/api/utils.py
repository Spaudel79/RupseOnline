from django.http import QueryDict
import json
from rest_framework import parsers

class MultipartJsonParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = {}
        # print(result.data)
        # for case1 with nested serializers
        # parse each field with json
        raw =[]
        flag = True
        for key, value in result.data.items():

            if type(value) != str:
                data[key] = value
                continue
            if '{' in value or "[" in value:
                try:
                    data[key] = json.loads(value)
                except ValueError:
                    data[key] = value
            if '[' in key :
                x=0
                s=key
                while x < len(key):
                    s = s.translate({ord('['): None})
                    s = s.translate({ord(']'): None})
                    s = s.translate({ord('0'): None})
                    s = s.translate({ord('1'): None})
                    s = s.translate({ord('2'): None})
                    s = s.translate({ord('3'): None})
                    s = s.translate({ord('4'): None})
                    s = s.translate({ord('5'): None})
                    x += 1
                key =s

                try:
                    dummy = json.loads(value)
                    if flag:
                        data[key] =[]
                        flag = False
                    data[key].append(dummy)
                    raw.append(dummy)


                except ValueError:
                    data[key] = value
            else:
                data[key] = value

        # if raw:
        #     data[key]=[]
        #     data[key].extend(raw)

        
        return parsers.DataAndFiles(data, result.files)