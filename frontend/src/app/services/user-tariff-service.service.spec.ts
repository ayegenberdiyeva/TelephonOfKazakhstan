import { TestBed } from '@angular/core/testing';

import { UserTariffServiceService } from './user-tariff-service.service';

describe('UserTariffServiceService', () => {
  let service: UserTariffServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UserTariffServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
