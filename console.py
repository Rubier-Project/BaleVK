import json

class Console(object):
    def __init__(self) -> None:
        pass

    def flex(self, obj: dict | list | str = {} or [] or "",
             flex_indent: int = None):
        
        assert type(obj) in (dict,
                             list,
                             str), exit("Object Type not Available: ( dict, list, str )")
        
        assert type(flex_indent) == int or flex_indent is None, exit("Flex Size Type not Available: ( int )")

        if type(obj) == dict:
            if len(obj.keys()) == 0:return obj
            else:
                print(json.dumps(obj, indent=flex_indent))
            
        elif type(obj) == list:
            if len(obj) == 0:return obj
            else:
                print(json.dumps(obj, indent=flex_indent))
            
        elif type(obj) == str:
            if ( obj.startswith("{") and obj.endswith("}") ) or ( obj.startswith("[") and obj.endswith("]") ):
                print(json.dumps(eval(obj), indent=flex_indent))
            
            else:
                exit("Object Syntax not Dictionary or List: ( dict, list )")