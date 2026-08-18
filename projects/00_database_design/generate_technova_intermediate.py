"""
TECHNOVA ENTERPRISE DATASET GENERATOR (PRODUCTION-GRADE)
=========================================================
Generates synthetic CSV datasets (June 2018 - June 2026).

Updates:
- Guaranteed Base Customers on Day 1 to prevent validation bypass.
- Optimized Customer Lookup for 100% Integrity Rule Compliance.
"""

import csv
import random
import sys
import math
from datetime import date, timedelta
from pathlib import Path

try:
    from tqdm import tqdm
except ImportError:
    print("\nERROR: tqdm belum terinstall. Install dengan: pip install tqdm")
    sys.exit(1)

# ============================================================
# CONFIGURATION
# ============================================================

RANDOM_SEED = 20260815

EMPLOYEE_ID_PREFIX = "EMP"
DEPARTMENT_ID_PREFIX = "DEP"
COUNTRY_ID_PREFIX = "CTR"
CITY_ID_PREFIX = "CTY"
CATEGORY_ID_PREFIX = "CAT"
PRODUCT_ID_PREFIX = "PRD"
CUSTOMER_ID_PREFIX = "CUS"
ORDER_ID_PREFIX = "OD"
ORDER_ITEM_ID_PREFIX = "OI"

MASTER_SEQUENCE_WIDTH = 5

OUTPUT_DIR = "technova_enterprise_dataset"
BEGINNER_EMPLOYEE_FILE = "technova_employees.csv"
NAME_POOL_FILE = "name_pool.csv"

# ---------- ROW COUNTS ----------
CUSTOMER_COUNT = 5000
PRODUCT_COUNT = 100
ORDER_COUNT = 100000

MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5
EXTRA_EMPLOYEES_PER_NEW_DEPARTMENT = 5

# ---------- DATE RANGE ----------
DATASET_START_DATE = "2018-06-01"
DATASET_END_DATE = "2026-06-30"

CUSTOMER_SIGNUP_START = "2018-06-01"
CUSTOMER_SIGNUP_END = "2026-06-15"

PRODUCT_CREATED_START = "2018-01-01"
PRODUCT_CREATED_END = "2024-12-31"

ORDER_DATE_START = "2018-06-01"
ORDER_DATE_END = "2026-06-30"

EXTRA_DEPARTMENTS = ["Customer Success", "Product"]

CUSTOMERS_WITHOUT_ORDERS = 150
PRODUCTS_WITHOUT_ORDERS = 2

CATEGORY_NAMES = [
    "Laptops", "Smartphones", "Computer Accessories", "Networking",
    "Software", "Office Equipment", "Storage", "Monitors"
]

PAYMENT_METHODS = ["Bank Transfer", "Credit Card", "E-Wallet", "Virtual Account"]

COUNTRIES = [
    {"country_id": 1, "country_name": "Indonesia"},
    {"country_id": 2, "country_name": "Singapore"},
    {"country_id": 3, "country_name": "Malaysia"},
    {"country_id": 4, "country_name": "Philippines"},
]

CITIES = [
    {"city_id": 1, "city_name": "Jakarta", "country_id": 1},
    {"city_id": 2, "city_name": "Bandung", "country_id": 1},
    {"city_id": 3, "city_name": "Surabaya", "country_id": 1},
    {"city_id": 4, "city_name": "Medan", "country_id": 1},
    {"city_id": 5, "city_name": "Semarang", "country_id": 1},
    {"city_id": 6, "city_name": "Yogyakarta", "country_id": 1},
    {"city_id": 7, "city_name": "Makassar", "country_id": 1},
    {"city_id": 8, "city_name": "Denpasar", "country_id": 1},
    {"city_id": 9, "city_name": "Palembang", "country_id": 1},
    {"city_id": 10, "city_name": "Malang", "country_id": 1},
    {"city_id": 11, "city_name": "Singapore", "country_id": 2},
    {"city_id": 12, "city_name": "Kuala Lumpur", "country_id": 3},
    {"city_id": 13, "city_name": "George Town", "country_id": 3},
    {"city_id": 14, "city_name": "Manila", "country_id": 4},
]

OVERSEAS_CUSTOMER_COUNTS = {11: 80, 12: 60, 13: 40, 14: 50}
EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com"]

# ---------- OVERSEAS NAME POOLS ----------
OVERSEAS_NAME_POOLS = {
    "Singapore": {
        "Male": {
            "first": ["Wei", "Kevin", "Jason", "Marcus", "Darren", "Ethan", "Jun Wei", "Bryan", "Aaron", "Daniel"],
            "last": ["Tan", "Lim", "Lee", "Ng", "Wong", "Chua", "Teo", "Tay", "Ong", "Goh"]
        },
        "Female": {
            "first": ["Chloe", "Rachel", "Jessica", "Hui Ling", "Megan", "Xin Yi", "Sarah", "Grace", "Amanda", "Samantha"],
            "last": ["Tan", "Lim", "Lee", "Ng", "Wong", "Chua", "Teo", "Tay", "Ong", "Goh"]
        }
    },
    "Malaysia": {
        "Male": {
            "first": ["Amirul", "Firdaus", "Khairul", "Zul", "Chong", "Wei Lun", "Suresh", "Hafiz", "Adam", "Danish"],
            "last": ["Ismail", "Abdullah", "Ahmad", "Tan", "Lee", "Wong", "Raj", "Chee", "Ibrahim", "Hassan"]
        },
        "Female": {
            "first": ["Nurul", "Fatin", "Farah", "Siti", "Mei Ling", "Anisa", "Priya", "Nadia", "Isha", "Sarah"],
            "last": ["Ismail", "Abdullah", "Ahmad", "Tan", "Lee", "Wong", "Subramaniam", "Hassan", "Razak", "Yusof"]
        }
    },
    "Philippines": {
        "Male": {
            "first": ["Mark", "John", "Christian", "Angelo", "Paolo", "Joshua", "Gabriel", "Miguel", "Carl", "Jose"],
            "last": ["Santos", "Reyes", "Cruz", "Bautista", "Garcia", "Mendoza", "Torres", "Flores", "Castillo", "Ramos"]
        },
        "Female": {
            "first": ["Maria", "Angel", "Princess", "Samantha", "Nicole", "Bea", "Alyssa", "Andrea", "Camille", "Patricia"],
            "last": ["Santos", "Reyes", "Cruz", "Bautista", "Garcia", "Mendoza", "Torres", "Flores", "Castillo", "Ramos"]
        }
    }
}

PRODUCT_PREFIXES = {
    "Laptops": ["TechNova Pro", "TechNova Air", "TechNova Work"],
    "Smartphones": ["TechNova X", "TechNova S", "TechNova Note"],
    "Computer Accessories": ["TechNova Mouse", "TechNova Keyboard", "TechNova Hub"],
    "Networking": ["TechNova Router", "TechNova Switch", "TechNova Access"],
    "Software": ["TechNova Suite", "TechNova Security", "TechNova Cloud"],
    "Office Equipment": ["TechNova Printer", "TechNova Scanner", "TechNova Desk"],
    "Storage": ["TechNova SSD", "TechNova Drive", "TechNova Storage"],
    "Monitors": ["TechNova View", "TechNova Ultra", "TechNova Office"],
}

PRICE_RANGES = {
    "Laptops": (7_000_000, 25_000_000),
    "Smartphones": (2_500_000, 18_000_000),
    "Computer Accessories": (100_000, 2_500_000),
    "Networking": (300_000, 8_000_000),
    "Software": (250_000, 6_000_000),
    "Office Equipment": (500_000, 12_000_000),
    "Storage": (400_000, 6_000_000),
    "Monitors": (1_500_000, 12_000_000),
}

NEW_DEPARTMENT_JOBS = {
    "Customer Success": ["Customer Success Specialist", "Customer Success Lead"],
    "Product": ["Product Analyst", "Product Specialist"],
}

rng = random.Random(RANDOM_SEED)
SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = SCRIPT_DIR / OUTPUT_DIR

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def parse_date(value):
    return date.fromisoformat(value) if isinstance(value, str) else value

def master_id(prefix, number):
    return f"{prefix}-{number:0{MASTER_SEQUENCE_WIDTH}d}"

def customer_date_id(date_value, sequence):
    return f"{CUSTOMER_ID_PREFIX}-{date_value.strftime('%y%m%d')}{sequence:03d}"

def order_date_id(date_value, sequence):
    return f"{ORDER_ID_PREFIX}-{date_value.strftime('%y%m%d')}{sequence:04d}"

def money(value):
    return round(float(value), 2)

def weighted_choice(items):
    values = [item[0] for item in items]
    weights = [item[1] for item in items]
    return rng.choices(values, weights=weights, k=1)[0]

def get_event_discount(order_date):
    dt = parse_date(order_date)
    if dt.day == dt.month:
        return 0.10
    if dt.month == 12 and dt.day >= 25:
        return 0.15
    return 0.00

def generate_date_with_growth(start_str, end_str, is_order=False):
    start = parse_date(start_str)
    end = parse_date(end_str)
    total_days = (end - start).days

    dates = [start + timedelta(days=i) for i in range(total_days + 1)]
    weights = []

    YEAR_GROWTH = {
        2018: 0.80,
        2019: 1.10,
        2020: 1.40,
        2021: 1.70,
        2022: 2.00,
        2023: 2.30,
        2024: 2.60,
        2025: 2.90,
        2026: 3.20
    }

    for d in dates:
        if is_order:
            base_weight = YEAR_GROWTH.get(d.year, 1.00)
            month_progress = (d.month - 1) / 11.0
            base_weight *= (1 + (month_progress * 0.25))

            if d.day == d.month:
                twin_multiplier = rng.uniform(2.5, 4.0)
                base_weight *= twin_multiplier
            elif d.month == 12 and d.day >= 25:
                yearend_multiplier = rng.uniform(3.5, 5.0)
                base_weight *= yearend_multiplier
            elif d.day in [25, 26, 27]:
                payday_multiplier = rng.uniform(1.5, 2.2)
                base_weight *= payday_multiplier
        else:
            year_idx = d.year - 2018
            month_progress = (d.month - 1) / 11.0
            base_weight = 1.0 + (year_idx * 0.4) + (month_progress * 0.2)

        weights.append(base_weight)

    return rng.choices(dates, weights=weights, k=1)[0]

def load_name_pool():
    path = SCRIPT_DIR / NAME_POOL_FILE
    if not path.exists():
        raise FileNotFoundError(f"File '{NAME_POOL_FILE}' tidak ditemukan di folder yang sama!")

    pool = {"Male": {"first": [], "last": []}, "Female": {"first": [], "last": []}}

    with path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            gender = row["gender"].strip().capitalize()
            position = row.get("position", "").strip().lower()

            if gender in pool:
                if position == "first":
                    pool[gender]["first"].append(name)
                elif position == "last":
                    pool[gender]["last"].append(name)
                else:
                    pool[gender]["first"].append(name)
                    pool[gender]["last"].append(name)

    for g in ["Male", "Female"]:
        if not pool[g]["first"]:
            pool[g]["first"] = ["Budi" if g == "Male" else "Siti"]
        if not pool[g]["last"]:
            pool[g]["last"] = ["Utomo" if g == "Male" else "Lestari"]

    return pool

def generate_person_name(name_pool, gender, city_id=None):
    if city_id == master_id(CITY_ID_PREFIX, 11):
        pool = OVERSEAS_NAME_POOLS["Singapore"][gender]
    elif city_id in (master_id(CITY_ID_PREFIX, 12), master_id(CITY_ID_PREFIX, 13)):
        pool = OVERSEAS_NAME_POOLS["Malaysia"][gender]
    elif city_id == master_id(CITY_ID_PREFIX, 14):
        pool = OVERSEAS_NAME_POOLS["Philippines"][gender]
    else:
        pool = name_pool[gender]

    first = rng.choice(pool["first"])
    last_options = [name for name in pool["last"] if name != first]
    if not last_options:
        last_options = pool["last"]

    last = rng.choice(last_options)
    return first, last

def write_csv(filename, rows, fieldnames):
    path = OUTPUT_PATH / filename
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in tqdm(rows, desc=f"Writing {filename}", unit="row"):
            writer.writerow(row)

# ============================================================
# DATA GENERATORS
# ============================================================

def load_beginner_employees():
    path = SCRIPT_DIR / BEGINNER_EMPLOYEE_FILE
    if not path.exists():
        raise FileNotFoundError(f"File employee awal '{BEGINNER_EMPLOYEE_FILE}' tidak ditemukan.")
    with path.open("r", newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))

def generate_departments(beginner_employees):
    existing_names = []
    for row in beginner_employees:
        name = row["department"].strip()
        if name and name not in existing_names:
            existing_names.append(name)
    for department_name in EXTRA_DEPARTMENTS:
        if department_name not in existing_names:
            existing_names.append(department_name)
    return [{"department_id": master_id(DEPARTMENT_ID_PREFIX, i), "department_name": name}
            for i, name in enumerate(tqdm(existing_names, desc="Generating departments"), start=1)]

def generate_employees(beginner_employees, departments, cities, name_pool):
    dept_map = {row["department_name"]: row["department_id"] for row in departments}
    city_map = {c["city_name"].lower(): c["city_id"] for c in cities}
    default_city_id = cities[0]["city_id"]

    rows = []
    next_sequence = 1

    for employee in tqdm(beginner_employees, desc="Copying Beginner employees"):
        c_name = employee["city"].strip().lower()
        c_id = city_map.get(c_name, default_city_id)

        rows.append({
            "employee_id": master_id(EMPLOYEE_ID_PREFIX, next_sequence),
            "first_name": employee["first_name"],
            "last_name": employee["last_name"],
            "email": employee["email"],
            "phone_number": employee["phone_number"],
            "gender": employee["gender"],
            "department_id": dept_map[employee["department"].strip()],
            "job_title": employee["job_title"],
            "salary": employee["salary"],
            "hire_date": employee["hire_date"],
            "city_id": c_id,
            "age": employee["age"],
        })
        next_sequence += 1

    all_city_ids = [c["city_id"] for c in cities]
    for department_name in tqdm(EXTRA_DEPARTMENTS, desc="Generating new-department employees"):
        for _ in range(EXTRA_EMPLOYEES_PER_NEW_DEPARTMENT):
            gender = rng.choice(["Male", "Female"])
            first, last = generate_person_name(name_pool, gender)
            hire = generate_date_with_growth("2018-06-01", "2026-05-31")

            rows.append({
                "employee_id": master_id(EMPLOYEE_ID_PREFIX, next_sequence),
                "first_name": first,
                "last_name": last,
                "email": f"{first.lower()}.{last.lower()}{next_sequence}@technova.com",
                "phone_number": f"08{rng.randint(1000000000, 9999999999)}",
                "gender": gender,
                "department_id": dept_map[department_name],
                "job_title": rng.choice(NEW_DEPARTMENT_JOBS.get(department_name, ["Staff"])),
                "salary": rng.randint(6_000_000, 14_000_000),
                "hire_date": hire.isoformat(),
                "city_id": rng.choice(all_city_ids),
                "age": rng.randint(23, 38),
            })
            next_sequence += 1

    return rows

def generate_categories():
    return [{"category_id": master_id(CATEGORY_ID_PREFIX, i), "category_name": name}
            for i, name in enumerate(tqdm(CATEGORY_NAMES, desc="Generating categories"), start=1)]

def generate_products(categories):
    rows = []
    for number in tqdm(range(1, PRODUCT_COUNT + 1), desc="Generating products"):
        category = categories[(number - 1) % len(categories)]
        cat_name = category["category_name"]
        prefix = rng.choice(PRODUCT_PREFIXES[cat_name])
        model = rng.choice(["100", "200", "300", "Pro", "Max", "Ultra", "Lite", "Prime"])
        low, high = PRICE_RANGES[cat_name]
        price = rng.randint(low // 1000, high // 1000) * 1000

        if number <= 15:
            created = parse_date("2018-01-01") + timedelta(days=rng.randint(0, 120))
        else:
            created = generate_date_with_growth(PRODUCT_CREATED_START, PRODUCT_CREATED_END)

        rows.append({
            "product_id": master_id(PRODUCT_ID_PREFIX, number),
            "product_name": f"{prefix} {model}",
            "category_id": category["category_id"],
            "price": money(price),
            "stock_quantity": rng.randint(0, 300),
            "created_date": created.isoformat(),
        })

    if rows:
        rows[0]["stock_quantity"] = 0
    return rows

def generate_countries():
    return [{"country_id": master_id(COUNTRY_ID_PREFIX, c["country_id"]), "country_name": c["country_name"]}
            for c in tqdm(COUNTRIES, desc="Generating countries")]

def generate_cities():
    return [{"city_id": master_id(CITY_ID_PREFIX, c["city_id"]), "city_name": c["city_name"], "country_id": master_id(COUNTRY_ID_PREFIX, c["country_id"])}
            for c in tqdm(CITIES, desc="Generating cities")]

def generate_customers(cities, name_pool):
    formatted_overseas = {master_id(CITY_ID_PREFIX, cid): count for cid, count in OVERSEAS_CUSTOMER_COUNTS.items()}
    overseas_city_ids = set(formatted_overseas.keys())
    domestic_city_ids = [c["city_id"] for c in cities if c["city_id"] not in overseas_city_ids]

    customer_city_ids = []
    for f_cid, count in formatted_overseas.items():
        customer_city_ids.extend([f_cid] * count)

    for _ in range(CUSTOMER_COUNT - len(customer_city_ids)):
        customer_city_ids.append(rng.choice(domestic_city_ids))
    rng.shuffle(customer_city_ids)

    # Menjamin 20 Customer pertama sudah terdaftar persis di hari pembukaan (1 Juni 2018)
    base_start_date = parse_date(CUSTOMER_SIGNUP_START)
    signup_dates = [base_start_date for _ in range(20)]
    signup_dates += [generate_date_with_growth(CUSTOMER_SIGNUP_START, CUSTOMER_SIGNUP_END, is_order=False) for _ in range(CUSTOMER_COUNT - 20)]
    signup_dates.sort()

    date_sequences = {}
    rows = []

    for idx, (city_id, signup_date) in enumerate(tqdm(zip(customer_city_ids, signup_dates), total=CUSTOMER_COUNT, desc="Generating customers"), start=1):
        date_sequences[signup_date] = date_sequences.get(signup_date, 0) + 1
        gender = rng.choice(["Male", "Female"])

        first, last = generate_person_name(name_pool, gender, city_id=city_id)

        first_clean = first.lower().replace(" ", "")
        last_clean = last.lower().replace(" ", "")

        rows.append({
            "customer_id": customer_date_id(signup_date, date_sequences[signup_date]),
            "first_name": first,
            "last_name": last,
            "gender": gender,
            "email": f"{first_clean}.{last_clean}{idx}@{rng.choice(EMAIL_DOMAINS)}",
            "phone": f"08{rng.randint(1000000000, 9999999999)}",
            "city_id": city_id,
            "signup_date": signup_date.isoformat(),
        })

    return rows

def generate_orders(customers):
    inactive_count = min(CUSTOMERS_WITHOUT_ORDERS, len(customers))
    inactive_customer_ids = set(c["customer_id"] for c in rng.sample(customers, k=inactive_count))
    active_customers = [c for c in customers if c["customer_id"] not in inactive_customer_ids]

    # Pre-sort customers berdasarkan tanggal signup
    sorted_customers = sorted(
        [{"customer_id": c["customer_id"], "signup_date": parse_date(c["signup_date"])} for c in active_customers],
        key=lambda x: x["signup_date"]
    )

    raw_orders = []
    max_order_date = parse_date(ORDER_DATE_END)

    for _ in tqdm(range(ORDER_COUNT), desc="Generating order dates & details"):
        order_date = generate_date_with_growth(ORDER_DATE_START, ORDER_DATE_END, is_order=True)

        # Hanya ambil dari customer yang signup <= order_date (100% garansi terisi)
        eligible_custs = [c for c in sorted_customers if c["signup_date"] <= order_date]
        chosen_cust = rng.choice(eligible_custs)

        days_diff = (max_order_date - order_date).days

        if days_diff <= 14:
            status = weighted_choice([
                ("Completed", 0.40),
                ("Shipped", 0.35),
                ("Processing", 0.20),
                ("Cancelled", 0.05),
            ])
        else:
            status = weighted_choice([
                ("Completed", 0.90),
                ("Cancelled", 0.07),
                ("Returned", 0.03),
            ])

        raw_orders.append({
            "customer_id": chosen_cust["customer_id"],
            "order_date": order_date,
            "status": status,
            "payment_method": rng.choice(PAYMENT_METHODS),
        })

    raw_orders.sort(key=lambda x: x["order_date"])

    date_sequences = {}
    rows = []
    for order_data in tqdm(raw_orders, desc="Formatting order IDs"):
        o_date = order_data["order_date"]
        date_sequences[o_date] = date_sequences.get(o_date, 0) + 1

        rows.append({
            "order_id": order_date_id(o_date, date_sequences[o_date]),
            "customer_id": order_data["customer_id"],
            "order_date": o_date.isoformat(),
            "status": order_data["status"],
            "payment_method": order_data["payment_method"],
        })

    return rows

def generate_order_items(orders, products):
    allowed_products = products[:len(products) - PRODUCTS_WITHOUT_ORDERS]
    rows = []
    next_sequence = 1

    for order in tqdm(orders, desc="Generating order items"):
        order_dt = parse_date(order["order_date"])
        discount_percent = get_event_discount(order_dt)

        eligible_products = [
            p for p in allowed_products
            if parse_date(p["created_date"]) <= order_dt
        ]

        if not eligible_products:
            raise RuntimeError(
                f"Tidak ada product yang tersedia pada "
                f"order_date {order_dt}."
            )

        item_count = min(rng.randint(MIN_ITEMS_PER_ORDER, MAX_ITEMS_PER_ORDER), len(eligible_products))
        chosen_products = rng.sample(eligible_products, k=item_count)

        for product in chosen_products:
            base_price = float(product["price"])

            rows.append({
                "order_item_id": master_id(ORDER_ITEM_ID_PREFIX, next_sequence),
                "order_id": order["order_id"],
                "product_id": product["product_id"],
                "quantity": rng.randint(1, 5),
                "unit_price": money(base_price),
                "discount_percent": money(discount_percent),
            })
            next_sequence += 1

    return rows

# ============================================================
# COMPREHENSIVE PRE-EXPORT VALIDATION ENGINE
# ============================================================

def validate_data_comprehensive(departments, employees, countries, cities, customers, categories, products, orders, order_items):
    print("\n" + "=" * 75)
    print("RUNNING STRICT PRE-EXPORT INTEGRITY VALIDATION ENGINE")
    print("=" * 75)

    cust_map = {c["customer_id"]: c for c in customers}
    prod_map = {p["product_id"]: p for p in products}
    ord_map = {o["order_id"]: o for o in orders}

    v1_passed = all(parse_date(o["order_date"]) >= parse_date(cust_map[o["customer_id"]]["signup_date"]) for o in orders)
    v2_passed = all(parse_date(ord_map[oi["order_id"]]["order_date"]) >= parse_date(prod_map[oi["product_id"]]["created_date"]) for oi in order_items)

    max_order_date = parse_date(ORDER_DATE_END)
    v3_passed = all(o["status"] not in ("Processing", "Shipped") or (max_order_date - parse_date(o["order_date"])).days <= 14 for o in orders)

    v4_passed = True
    for oi in order_items:
        o_date = parse_date(ord_map[oi["order_id"]]["order_date"])
        if o_date.day == o_date.month:
            if float(oi["discount_percent"]) != 0.10:
                v4_passed = False
                break

    v5_passed = True
    for oi in order_items:
        o_date = parse_date(ord_map[oi["order_id"]]["order_date"])
        if o_date.month == 12 and o_date.day >= 25:
            if float(oi["discount_percent"]) != 0.15:
                v5_passed = False
                break

    city_country_map = {c["city_id"]: c["country_id"] for c in cities}
    v6_passed = all(c["city_id"] in city_country_map for c in customers)

    v7_passed = len(customers) == len({c["customer_id"] for c in customers})
    v8_passed = len(orders) == len({o["order_id"] for o in orders})

    v9_passed = True
    date_counts = {}
    for o in orders:
        dt = parse_date(o["order_date"])
        seq = int(o["order_id"].split("-")[1][6:])
        date_counts[dt] = date_counts.get(dt, 0) + 1
        if seq != date_counts[dt]:
            v9_passed = False
            break

    checks = [
        ("Customer Signup <= Order Date", v1_passed),
        ("Product Created <= Order Date", v2_passed),
        ("Historical Order Status", v3_passed),
        ("Twin-Date Discount = 10%", v4_passed),
        ("Year-End Discount = 15%", v5_passed),
        ("Foreign Customer Location Integrity", v6_passed),
        ("Customer ID Uniqueness", v7_passed),
        ("Order ID Uniqueness", v8_passed),
        ("Daily Order Sequence", v9_passed),
    ]

    all_passed = True
    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}")
        if not passed:
            all_passed = False

    print("=" * 75)
    if not all_passed:
        raise RuntimeError("Validasi gagal! Terdapat ketidakcocokan logika pada dataset yang dihasilkan.")

def main():
    try:
        name_pool = load_name_pool()
        beginner_employees = load_beginner_employees()

        countries = generate_countries()
        cities = generate_cities()
        departments = generate_departments(beginner_employees)
        employees = generate_employees(beginner_employees, departments, cities, name_pool)
        categories = generate_categories()
        products = generate_products(categories)
        customers = generate_customers(cities, name_pool)
        orders = generate_orders(customers)
        order_items = generate_order_items(orders, products)

        validate_data_comprehensive(departments, employees, countries, cities, customers, categories, products, orders, order_items)

        OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
        write_csv("departments.csv", departments, ["department_id", "department_name"])
        write_csv("employees.csv", employees, ["employee_id", "first_name", "last_name", "email", "phone_number", "gender", "department_id", "job_title", "salary", "hire_date", "city_id", "age"])
        write_csv("countries.csv", countries, ["country_id", "country_name"])
        write_csv("cities.csv", cities, ["city_id", "city_name", "country_id"])
        write_csv("customers.csv", customers, ["customer_id", "first_name", "last_name", "gender", "email", "phone", "city_id", "signup_date"])
        write_csv("categories.csv", categories, ["category_id", "category_name"])
        write_csv("products.csv", products, ["product_id", "product_name", "category_id", "price", "stock_quantity", "created_date"])
        write_csv("orders.csv", orders, ["order_id", "customer_id", "order_date", "status", "payment_method"])
        write_csv("order_items.csv", order_items, ["order_item_id", "order_id", "product_id", "quantity", "unit_price", "discount_percent"])

        print("\nENTERPRISE DATASET GENERATION COMPLETE & READY FOR PORTFOLIO!")
    except Exception as e:
        print(f"\nGENERATION FAILED: {e}")

    input("\nPRESS ENTER TO CLOSE THIS WINDOW")

if __name__ == "__main__":
    main()