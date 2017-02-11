from fakturoid import Fakturoid
from datetime import date
from fakturoid import Invoice, InvoiceLine

fa = Fakturoid(slug='mergadobackend1', email='peter.smatana@mergado.com',
               api_key='bd5a4ef76c536c15c7a2ed835af4e78f7397fb08',
               )


def print_all_invoices(fakturoid):
    for invoice in fakturoid.invoices(proforma=False, since=date(2013,1,1)):
        print(invoice.number, invoice.total)

# print_all_invoices(fa)


def create_invoice():
    invoice = Invoice(
        client_name='Reglendo technologies, s.r.o.',
        subject_id=2023409,
        number='2013-0108',
        due=10,
        issued_on=date(2017, 3, 3),
        taxable_fulfillment_due=date(2017, 3, 3),
        lines=[
            # use Decimal or string for floating values
            InvoiceLine(name='Hard work',
                        unit_name='h',
                        unit_price=40000,
                        vat_rate=20),
            InvoiceLine(name='Soft material',
                        quantity=12,
                        unit_name='ks',
                        unit_price="4.60",
                        vat_rate=20),
        ]
    )
    fa.save(invoice)

    print(invoice.due_on)

create_invoice()
