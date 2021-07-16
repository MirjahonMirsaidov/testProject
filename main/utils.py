from django.core.exceptions import ObjectDoesNotExist

from .models import Samples, Items, Category


def add_category(item, category, parent=None):
    cat_name = category.replace('\r', '')
    # check if category is not empty or None
    if cat_name:
        # check if category exists or not
        if Category.objects.filter(name=cat_name).exists():
            cat = Category.objects.get(name=cat_name)
        else:
            cat = Category.objects.create(
                name=category.replace('\r', ''),
                parent=parent
            )
        # check if item has category
        if not item.categories.filter(name=cat_name).exists():
            item.categories.add(cat)


def write_samples_from_tsv(tsv_file):
    tsv_file = tsv_file.read().decode('utf-8')
    data = tsv_file.split('\n')

    for row in data:
        fields = row.split('\t')
        try:
            id, item_id, date, name, text = fields
            if Samples.objects.filter(id=id).exists():
                sample = Samples.objects.get(id=id)
                sample.item_id = item_id
                sample.date = date
                sample.name = name
                sample.text = text.replace('\r', '')
                sample.save()
            else:
                Samples.objects.create(
                    id=id,
                    item_id=item_id,
                    date=date,
                    name=name,
                    text=text.replace('\r', '')
                )
        except:
            continue


def write_items_from_tsv(tsv_file):
    tsv_file = tsv_file.read().decode('utf-8')
    data = tsv_file.split('\n')

    for row in data:
        fields = row.split('\t')
        try:
            id, name, rank, quantity, verified, categories = fields
            if Items.objects.filter(id=id).exists():
                item = Items.objects.get(id=id)
                item.name = name
                item.quantity = quantity
                item.verified = verified
                item.save()
            else:
                item = Items.objects.create(
                    id=id,
                    name=name,
                    rank=rank,
                    quantity=quantity,
                    verified=verified,
                )
            categories = categories.split(';')
            for category in categories:
                # check if category has subcategory
                if '.' in category:
                    cat, subcat = category.split('.')
                    try:
                        parent = Category.objects.get_or_create(name=cat, parent=None)[0]
                        add_category(item, subcat, parent)
                    except ObjectDoesNotExist:
                        continue
                else:
                    add_category(item, category)

        except:
            continue




