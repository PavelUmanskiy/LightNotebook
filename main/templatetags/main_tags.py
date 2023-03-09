from django import template


register = template.Library()


@register.simple_tag()
def deal_balance(deal_budget: float, deal_expenses: float) -> float:
    return deal_budget - deal_expenses