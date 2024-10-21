
def all_thing_is_obj(object: any) -> int:
    # Retrieve object's type (itself a type)
	obj_type = type(object)

	# Respect subject representation of the type
	if obj_type == str:
		print(object, "is in the kitchen :", obj_type.__name__)
	elif obj_type == int:
		print("type not found")
	else:
		print(obj_type.__name__,":", obj_type)
	return (42)
