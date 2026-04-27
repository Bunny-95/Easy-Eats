# Product Requirement Specification (PRS)  
## Easy Eats – Smart Campus Food Ordering Platform

---

# 1. Document Purpose

This Product Requirement Specification (PRS) defines the functional, technical, and business requirements for the Easy Eats platform.

The goal of Easy Eats is to simplify campus food ordering through a digital system that enables fast ordering, secure payments, and quick pickup.

---

# 2. Product Name

**Easy Eats**

---

# 3. Product Objective

To provide a modern food ordering solution for college campuses that reduces waiting time, improves student convenience, and helps vendors manage orders efficiently.

---

# 4. Problem Being Solved

Current campus food purchasing systems often involve:

- Long queues during peak hours
- Manual order confusion
- Delayed service
- Limited payment flexibility
- Poor order visibility
- Customer dissatisfaction

Easy Eats addresses these issues through automation.

---

# 5. Target Users

## Primary Users

- Students
- Faculty
- Campus Staff

## Secondary Users

- Cafeteria Owners
- Kitchen Staff
- Campus Vendors

## Admin Users

- System Administrators
- Food Outlet Managers

---

# 6. Functional Requirements

## 6.1 User Authentication

- User registration
- Secure login system
- Role-based access (Student/Admin)
- Logout system

## 6.2 Restaurant Module

- View all available restaurants
- Display restaurant categories
- View restaurant menu
- Show availability status

## 6.3 Cart Module

- Add food items
- Increase / decrease quantity
- Remove items
- Auto price calculation

## 6.4 Order Module

- Place order
- Generate order ID
- Store order details
- Track order progress

## 6.5 Payment Module

- Razorpay payment integration
- UPI / Card / Wallet support
- Payment success confirmation
- Failed payment handling

## 6.6 Tracking Module

- Order accepted
- Preparing
- Ready for pickup
- Completed

## 6.7 Admin Dashboard

- View all orders
- Update order status
- Manage restaurants
- View completed orders

## 6.8 Chatbot Module

- Food suggestions
- FAQ support
- Order help

---

# 7. Non-Functional Requirements

## Performance

- Fast page loading
- Responsive UI
- Smooth mobile experience

## Security

- JWT authentication
- Protected routes
- Secure payment gateway

## Reliability

- Stable backend APIs
- Cloud database support

## Scalability

- Support multiple campuses
- Add multiple restaurants

## Usability

- Clean interface
- Beginner-friendly navigation

---

# 8. Technology Requirements

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- React Router

## Backend

- FastAPI
- Python

## Database

- PostgreSQL

## Deployment

- Vercel (Frontend)
- Render (Backend)

## Payment

- Razorpay

---

# 9. Database Requirements

## Main Tables

- Users
- Restaurants
- Menu Items
- Orders
- Order Items

---

# 10. User Flow

## Student Flow

Login → Browse Restaurants → Add to Cart → Pay → Track Order → Pickup

## Admin Flow

Login → View Orders → Update Status → Complete Order

---

# 11. UI Requirements

- Mobile responsive design
- Desktop support
- Modern layout
- Fast navigation
- Clean order tracking page

---

# 12. Constraints

- Requires internet connection
- Depends on payment gateway availability
- Initial rollout limited to campus users

---

# 13. Risks

- User adoption resistance
- Payment gateway downtime
- Incorrect order handling by staff

---

# 14. Success Metrics

- Reduced waiting time
- Increased digital orders
- Positive student feedback
- Faster order processing
- Vendor satisfaction

---

# 15. Future Enhancements

- AI recommendations
- Push notifications
- QR code pickup
- Subscription meals
- Loyalty rewards
- Analytics dashboard

---

# 16. Estimated Timeline

## Phase 1

Research + Interviews

## Phase 2

UI/UX + Development

## Phase 3

Testing + Deployment

## Phase 4

Pilot Launch

---

# 17. Conclusion

Easy Eats is a practical and scalable solution that modernizes campus food services by combining convenience, speed, and technology into one platform.

---

# Prepared By

Team Easy Eats  
| Name | SRN | Role |
|------|-----|------|
| Ullas | R23EF288 | Customer research + interviews |
| Srujan L | R23EF263 | GitHub + Backend + Frontend |
| Thejas M G | R23EF283 | Presentation|
| Shreyas D | R23EF252 | Customer research + interviews |
| Shreyas B R | R23EF251 | Customer research + interviews |
| Shashank Ganapati Naik | R23EF245 | Google Form + Testing |