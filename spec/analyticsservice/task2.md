# Task 2/17: `AnalyticsScheduleSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `schedule-source` |
| File | `analyticsservice/src/analytics_service/internal/functions/cron/analytics_schedule_source.py` |
| Test | `analyticsservice/tests/functions/test_cron/analytics_schedule_source.py` |
| Service | `Analytics Service` |


## Behaviour

Create an analytics job message identifying the local scheduled firing.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/cron/analytics_schedule_source.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_cron/analytics_schedule_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task2.md — AnalyticsScheduleSource — Python — done`