from medical.models import Service, Item


def get_service_of_category(category, valid=True):
    return Service.objects.filter(category=category).filter(validity_to__isnull=valid).first()


def get_item_of_type(item_type, valid=True):
    return Item.objects.filter(type=item_type).filter(validity_to__isnull=valid).first()


def create_test_service(category, valid=True, custom_props={}):
    custom_props = {k: v for k, v in custom_props.items() if hasattr(Service, k)} 
    code = custom_props.pop('code', ('TST-' + category))     
    obj = Service.objects.filter(code=code, validity_to__isnull=valid).first()
    if obj is not None:
        if custom_props:
            Service.objects.filter(id=obj.id).update(**custom_props)
            obj.refresh_from_db()
        return obj
    else:
        return Service.objects.create(
            **{
                "maximum_amount": 5000,
                "code": code,
                "category": category,
                "name": "Test service " + category,
                "type": Service.TYPE_CURATIVE,
                "level": 1,
                "price": 100,
                "patient_category": 15,
                "care_type": Service.CARE_TYPE_OUT_PATIENT,
                "validity_from": "2019-06-01",
                "validity_to": None if valid else "2019-06-01",
                "audit_user_id": -1,
                **custom_props
            }
        )


def create_test_item(item_type, valid=True, custom_props={}):
    custom_props = {k: v for k, v in custom_props.items() if hasattr(Item, k)} 
    code = custom_props.pop('code', 'XXX')
        
    obj = Item.objects.filter(code=code, validity_to__isnull=valid).first()
    if obj is not None:
        if custom_props:
            Item.objects.filter(id=obj.id).update(**custom_props)
            obj.refresh_from_db()
        return obj
    else:
        return Item.objects.create(
            **{
                "quantity":1,
                "maximum_amount":225000,
                "code": "XXX",
                "type": item_type,
                "name": "Test item",
                "price": 100,
                "patient_category": 15,
                "care_type": 1,
                "validity_from": "2019-06-01",
                "validity_to": None if valid else "2019-06-01",
                "audit_user_id": -1,
                **(custom_props if custom_props else {})
            }
        )
