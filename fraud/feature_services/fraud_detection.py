from tecton import FeatureService
from fraud.features.stream_window_aggregate_feature_views.user_transaction_amount_metrics import user_transaction_amount_metrics
from fraud.features.user_transaction_counts import user_transaction_counts
from fraud.features.stream_feature_views.last_transaction_amount_sql import last_transaction_amount_sql
# from fraud.features.user_has_good_credit import user_has_good_credit


fraud_detection_feature_service = FeatureService(
    name='fraud_detection_feature_service',
    features=[
        user_transaction_amount_metrics,
        user_transaction_counts,
        last_transaction_amount_sql
    ]
)


# fraud_detection_feature_service_v2 = FeatureService(
#     name='fraud_detection_feature_service:v2',
#     description='A FeatureService providing features for a model that predicts if a transaction is fraudulent.',
#     family='fraud',
#     tags={'release': 'production'},
#     features=[
#        user_has_good_credit, # New feature
#        user_transaction_amount_metrics,
#        user_transaction_counts,
#        last_transaction_amount_sql
#     ]
# )
