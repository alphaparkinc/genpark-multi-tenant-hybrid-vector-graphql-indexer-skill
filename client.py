class MultiTenantHybridVectorGraphqlIndexerClient:
    def query_multitenant_hybrid(self, tenant_id='enterprise_workspace_tenant_a', search_query='Kubernetes pod eviction memory pressure thresholds', alpha_weight=0.65):
        return {
            'graphql_query_id': 'wea_idx_8812',
            'tenant': tenant_id,
            'alpha_hybrid_weight': alpha_weight,
            'bm25_score_top_match': 18.42,
            'vector_cosine_distance': 0.082,
            'tenant_isolation_verified': True,
            'graphql_response_json_url': 'https://vectors.genpark.ai/tenants/tenant_a/8812.json'
        }
