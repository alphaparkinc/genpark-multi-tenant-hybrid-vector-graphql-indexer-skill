from client import MultiTenantHybridVectorGraphqlIndexerClient

def main():
    client = MultiTenantHybridVectorGraphqlIndexerClient()
    res = client.query_multitenant_hybrid('tenant_fintech_77', 'Securities trading settlement latency compliance rules', 0.5)
    print('Hybrid Vector Query: ' + res['graphql_query_id'] + ' | Tenant: ' + res['tenant'])
    print('Alpha Weight: ' + str(res['alpha_hybrid_weight']) + ' | BM25: ' + str(res['bm25_score_top_match']) + ' | Cosine: ' + str(res['vector_cosine_distance']))
    print('Tenant Isolated: ' + str(res['tenant_isolation_verified']))
    print('Response URL: ' + res['graphql_response_json_url'])

if __name__ == '__main__':
    main()
