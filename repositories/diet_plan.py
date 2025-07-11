import json
from typing import Optional, List
from tinybd import Query
from projeto.models import DietPlan
from projeto.repositories.base_repository import BaseRepository

class DietPlanRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.diet_plan_table = self.get_table('diet_plans')
        
    def create_diet_plan(self, telegram_id: int, plan_details: str) -> DietPlan:
        new_diet_plan = DietPlan(
            user_id = telegram_id_id,
            details = plan_details,
        )
        self.diet_plan_table.insert(json.loads(new_diet_plan.model_dump_json()))
        return new_diet_plan
    
    def get.diet_plan_by_id(self, plan_id: int) -> Optional[DietPlan]:
        DietPlanQuery = Query()
        result = self.diet_plan_table.get(DietPlanQuery.id == plan_id)
        return DietPlan(**result) if result else None

    def get_latest_diet_plan_for_user(self, telegram_id: int) -> Optional[DietPlan]:
        DietPlanQuery = Query()
        plans = self.diet_plan_table.search(DietPlanQuery.telegram_id == telegram_id)
        if not plans:
            return None
        
        latest_plan = sorted(plans, key=lambda plan: plan['created_at'], reverse=True)[0]
        return DietPlan(**latest_plan)
    
    def update_diet_plan(self, plan_id: int, plan_details: str) -> Optional[DietPlan]:
        DietPlanQuery = Query()
        self.diet_plan_table.update({'plan_details': plan_details}, DietPlanQuery.id == plan_id)
        update_plan = self.get_diet_plan_by_id(plan_id)
        return DietPlan(**update_plan)

    def delete_diet_plan(self, plan_id: int) -> None:
        DietPlanQuery = Query()
        self.Diet_plan_table.remove(DietPlanQuery.id == plan_id)

    def get_all_diet_plans(self) -> List[DietPlan]:
        all_plans = self.diet_plan_table.all()
        return[DietPlan(**plan) for plan in all_plans]
