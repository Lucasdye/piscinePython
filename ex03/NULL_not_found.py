def NULL_not_found(object: any)-> int:
	obj_type = type(object)

	if object == None:
		print("Nothing", ":", object, obj_type)
	elif obj_type == int and object == 0:
		print("Zero", ":", object, obj_type)
	elif obj_type == str and len(object) == 0:
		print("Empty", ":", obj_type)
	elif obj_type == float and object != object:
		print("Cheese", ":", object, obj_type)
	elif obj_type == bool and object == False:
		print("Fake", ":", object, obj_type)
	else:
		print("Type not found")
		return (1)
	return(0)