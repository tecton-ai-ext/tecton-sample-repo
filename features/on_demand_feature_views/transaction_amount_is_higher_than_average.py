from tecton import on_demand_feature_view, RequestSource, Field
from tecton.types import Float64, Bool
from features.stream_feature_views.user_transaction_amount_metrics import user_transaction_amount_metrics


transaction_request = RequestSource(schema=[Field('amount', Float64)])

@on_demand_feature_view(
    sources=[transaction_request, user_transaction_amount_metrics],
    mode='python',
    schema=[Field('transaction_amount_is_higher_than_average', Bool)],
    owner='matt@tecton.ai',
    tags={'release': 'production'},
    description='The transaction amount is higher than the 1 day average.'
)
def transaction_amount_is_higher_than_average(transaction_request, user_transaction_amount_metrics):
    amount_mean = 0 if user_transaction_amount_metrics['amount_mean_24h_10m'] == None else user_transaction_amount_metrics['amount_mean_24h_10m']
    return {'transaction_amount_is_higher_than_average': transaction_request['amount'] > amount_mean}
