"""Group Policies router — fetch, preview and execute multi-network policy copy."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from services.group_policy_service import GroupPolicyCopyService
from webapp.session import make_client, require_session

router = APIRouter(tags=["group_policies"])


class GroupPolicyRequest(BaseModel):
    selected_policies: list[dict[str, Any]]
    destination_networks: list[dict[str, Any]]


@router.get("/group-policies")
async def list_group_policies(
    network_id: str = Query(...),
    session=Depends(require_session),
) -> list:
    try:
        return make_client(session).get_group_policies(network_id)
    except Exception as exc:
        raise HTTPException(502, str(exc))


@router.post("/group-policies/preview")
async def gp_preview(body: GroupPolicyRequest, session=Depends(require_session)) -> list:
    try:
        svc = GroupPolicyCopyService(make_client(session))
        previews = svc.preview(body.selected_policies, body.destination_networks)
        return [
            {
                "network_id": p.network_id,
                "network_name": p.network_name,
                "new_count": p.new_count,
                "exists_count": p.exists_count,
                "invalid_count": p.invalid_count,
                "policy_statuses": [
                    {
                        "status": s.status,
                        "detail": s.detail,
                        "policy_name": s.policy.get("name"),
                    }
                    for s in p.policy_statuses
                ],
            }
            for p in previews
        ]
    except Exception as exc:
        raise HTTPException(502, str(exc))


@router.post("/group-policies/execute")
async def gp_execute(body: GroupPolicyRequest, session=Depends(require_session)) -> list:
    try:
        svc = GroupPolicyCopyService(make_client(session))
        results = svc.execute(body.selected_policies, body.destination_networks)
        return [
            {
                "network_id": r.network_id,
                "network_name": r.network_name,
                "success": r.success,
                "policies_added": r.policies_added,
                "policies_skipped": r.policies_skipped,
                "error": r.error,
            }
            for r in results
        ]
    except Exception as exc:
        raise HTTPException(502, str(exc))
