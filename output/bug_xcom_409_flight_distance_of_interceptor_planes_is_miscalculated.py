"""Kata - [BUG] XCOM-409: Flight distance of Interceptor planes is miscalculated

completed at: 2025-03-26 15:39:17
by: Barbora Hůlová

You are an intern working in the software development department of the X-COM agency, responsible for fighting off a large-scale invasion of extraterrestrials. Your task for today is described with the bug report below:

------

## [BUG] XCOM-409: Flight distance of Interceptor planes is miscalculated

**Type:**      Bug 🪳  
**Priority:**  Major  
**Component:** Operational Logistics Software  
**Reporter:**  `maverick`  
**Assignee:**  _Assigned to you_

---

### Bug Description

Pilots have reported discrepancies in their flight logs after returning from interception missions. The **travel distance** logged in the logistics software does not match actual flight paths, potentially leading to incorrect fuel calculations and errors in planning of future missions.

### Steps to Reproduce

1. Deploy an interceptor to engage a UFO.  
2. Upon its return, note the average speed (given in **knots**) and travel time (in **minutes**) reported by onboard instruments.  
3. Enter the values into the Logistics and Planning System.
4. Expected result: The system should correctly compute the **distance in kilometers**.  
5. Actual result: The logged distance appears **inaccurate**.

### Impact

If not fixed, this could cause interceptors to **run out of fuel mid-mission**, leaving Earth vulnerable to alien attacks. On the other hand, if the system **overestimates travel distance**, interceptors may be **overfueled**, making them heavier than necessary. This reduces **maneuverability**, increases **takeoff time**, and could put pilots at a disadvantage during high-speed engagements with alien craft.  

The Flight Operations team has requested an immediate fix.  

### Task

Investigate and fix the bug in the travel distance calculation function.

------

Once this ticket is resolved, you can pick another open ticket from the [backlog](https://www.codewars.com/collections/xcom-backlog). 

"""

# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*

def travel_distance(avg_speed, travel_time):
    return avg_speed * 1.852 * (travel_time / 60)
