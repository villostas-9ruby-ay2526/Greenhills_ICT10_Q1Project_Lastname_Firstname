from pyscript import display, document


#This will help calculate for the price
def get_reciept(e):
    prod_1 = (int.document.getElementbyId("first_option").value)
    prod_2 = (int.document.getElementbyId("second_option").value)
    prod_3 = (int.document.getElementbyId("third_option").value)
    subtotal = prod_1 + prod_2 + prod_3
    tax_rate = subtotal * 0.12
    total = subtotal + tax_rate


    display(f'Subtotal: {subtotal} Tax: {tax_rate}  Total: {total}' target='price')
