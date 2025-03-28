import { User } from './user';
import { TariffPlan } from './tariff-plan';

export interface Transaction {
    id: number;
    user: User;
    old_tariff?: TariffPlan | null;
    new_tariff: TariffPlan;
    price_paid: number;
    timestamp: string;
}
