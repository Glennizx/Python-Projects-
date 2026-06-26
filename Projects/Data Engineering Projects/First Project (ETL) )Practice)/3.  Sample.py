import pandas as pd

# ── 1. EXTRACT ───────────────────────────
def extract(filepath):
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} rows")
    return df


# ── 2. PROFILE ───────────────────────────
def profile(df):
    print("\n── PROFILE REPORT ──────────────────")

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nInvalid quantity (must be > 0):")
    print(df[df['quantity'] <= 0][['order_id', 'quantity']])

    print("\nUnique status values:")
    print(df['status'].unique())

    print("\nUnique date formats:")
    print(df['order_date'].unique())

    print("────────────────────────────────────")


# ── 3. TRANSFORM ─────────────────────────
def transform(df):
    # Fix casing
    df['customer_name'] = df['customer_name'].str.title().str.strip()
    df['email']         = df['email'].str.lower().str.strip()
    df['status']        = df['status'].str.lower().str.strip()

    # Fix nulls
    df['customer_name'] = df['customer_name'].fillna('Unknown')
    df['email']         = df['email'].fillna('no-email@unknown.com')

    # Fix invalid rows
    df = df[df['quantity'] > 0]

    # Fix dates
    df['order_date'] = pd.to_datetime(df['order_date'],
                                      infer_datetime_format=True)
    df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')

    # Add computed column
    df['total_amount'] = df['quantity'] * df['unit_price']

    print(f"✅ Transform done — {len(df)} clean rows")
    return df


# ── 4. LOAD ──────────────────────────────
def load(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"✅ Saved to {output_path}")


# ── RUN THE PIPELINE ─────────────────────
df = extract('data/raw_sales.csv')
profile(df)               # check BEFORE cleaning
df = transform(df)
profile(df)               # check AFTER cleaning  ← same function reused!
load(df, 'cleaned_sales.csv')