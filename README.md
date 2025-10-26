# Transfer Request Module for Odoo 17

A comprehensive internal transfer request management module for Odoo 17 with project integration and location-based access control.

## Features

### Core Features
- **Internal Transfer Requests**: Create and manage transfer requests between warehouse locations
- **Multi-state Workflow**: Draft → Waiting for Approval → Approved → Received/Cancelled
- **Location-based Access Control**: Users can only request/approve transfers for their assigned locations
- **Product Availability Check**: Real-time stock availability validation
- **Automatic Stock Picking**: Creates and validates stock pickings automatically

### Project Integration (New)
- **Project Linking**: Link transfer requests to specific projects
- **Product Validation**: Validate products against project's allowed product list
- **Project Smart Buttons**: View transfer requests directly from project view
- **Allowed Products Management**: Define which products can be transferred per project

### Additional Features
- **Mail Integration**: Full chatter support with activity tracking
- **Duplication Support**: Enhanced record duplication with proper field reset
- **User Location Assignment**: Support for multiple locations per user (Many2many)
- **Print Reports**: Generate stock picking reports
- **Demand Validation**: Prevent over-requesting products

## Installation

1. Copy the module to your Odoo addons directory:
   ```bash
   cp -r transfer_request /opt/odoo17/custom_addons/
   ```

2. Update the module list:
   - Go to Apps → Update Apps List

3. Install the module:
   - Search for "Transfer Request"
   - Click Install

## Configuration

### 1. User Location Setup

Users must be assigned to locations before they can create/approve transfer requests.

1. Go to **Settings → Users & Companies → Users**
2. Select a user
3. Add locations to the **Locations** field (Many2many)

### 2. Project Setup (Optional)

To use project integration:

1. Go to **Project → Projects**
2. Open or create a project
3. Go to **Allowed Products** tab
4. Add products that can be transferred for this project

### 3. Warehouse Configuration

Ensure you have:
- At least 2 stock locations configured
- Products with stock in source locations
- Operation types configured for internal transfers

## Usage

### Creating a Transfer Request

1. Go to **Inventory → Operations → Internal Transfer**
2. Click **Create**
3. Fill in the form:
   - **Project** (optional): Select project if applicable
   - **Operation Type**: Internal Transfers
   - **Source Location**: Where items come from
   - **Destination Location**: Where items go to
   - **Scheduled Date**: When transfer should happen

4. Add items:
   - Click **Items** tab → **Add a line**
   - Select **Product**
   - Check **Available Amount In source**
   - Enter **Demand** quantity

5. Click **Request** to submit for approval

### Approval Workflow

1. **Request** (by requester):
   - User must have access to destination location
   - Creates stock picking
   - State: Draft → Waiting for Approval

2. **Confirm** (by approver):
   - User must have access to source location
   - Validates stock picking
   - State: Waiting → Approved

3. **Receive** (by receiver):
   - User must have access to destination location
   - Marks transfer as complete
   - State: Approved → Received

### Project Integration

When a project is selected:

1. If project has **no allowed products** defined:
   - Any product can be transferred

2. If project **has allowed products** defined:
   - Only products in the allowed list can be transferred
   - Validation error shown if invalid products added

## Dependencies

- `product` - Product management
- `stock` - Inventory management
- `mail` - Chatter and activity tracking
- `project` - Project integration

## Technical Details

### Models

- `transfer.request` - Main transfer request model
- `transfer.request.item` - Transfer request line items
- `project.project` - Extended with allowed products
- `res.users` - Extended with location access

### Security

- Access rights defined in `security/ir.model.access.csv`
- Location-based access control via user location assignment

### Views

- Form view with state workflow buttons
- Tree/list view for transfer requests
- Project form view with transfer request smart button
- User form view with location assignment

## Version History

### Version 1.1
- Added project integration
- Added product validation against project allowed products
- Enhanced duplication with explicit field reset
- Improved copy behavior for line items
- Added project smart buttons
- Added allowed products management

### Version 1.0
- Initial release
- Basic transfer request workflow
- Location-based access control
- Stock picking integration
- Mail/chatter support

## Author

Teddy

## License

AGPL-3

## Support

For issues, questions, or contributions, please contact the module maintainer.

## Testing

See `TESTING_GUIDE.md` for comprehensive testing instructions.
