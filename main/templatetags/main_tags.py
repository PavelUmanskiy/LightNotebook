from django import template


register = template.Library()


@register.simple_tag
def deal_balance(deal_budget, deal_expenses):
    return deal_budget - deal_expenses