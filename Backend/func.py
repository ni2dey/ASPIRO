import torch
def recommend_domains(user_skills, model, data, node_mapping, reverse_mapping, combined_df, top_k=10):
    model.eval()
    with torch.no_grad():
        out = model(data.x, data.edge_index)

        # Get IDs of user skills present in node mapping
        skill_ids = [node_mapping[skill] for skill in user_skills if skill in node_mapping]
        if not skill_ids:
            return []

        user_vec = out[skill_ids].mean(dim=0)

        domain_scores = []
        for domain in combined_df.columns:
            matching_skills = []
            for skill in user_skills:
                if skill in combined_df.index and domain in combined_df.columns:
                    if combined_df.at[skill, domain] >= 0.5:
                        matching_skills.append(skill)

            if len(matching_skills) >= 2 and domain in node_mapping:
                domain_id = node_mapping[domain]
                domain_vec = out[domain_id]
                score = torch.dot(domain_vec, user_vec).item()
                domain_scores.append((domain, score))

        domain_scores.sort(key=lambda x: x[1], reverse=True)
        recommended_domains = [domain for domain, _ in domain_scores[:top_k]]
        return recommended_domains
