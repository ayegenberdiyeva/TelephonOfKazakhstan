import { User } from './user';
import { TariffPlan } from './tariff-plan';

export interface UserTariffPlan {
    id: number;
    user: User;
    tariffPlan: TariffPlan;
    startDate: string;
    is_active: boolean;
}
